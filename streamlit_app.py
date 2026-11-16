# streamlit_app.py
import json
from pathlib import Path

import joblib
import numpy as np
import streamlit as st
import torch
import open_clip
from PIL import Image

# ---------- config ----------
APP_DIR = Path(__file__).parent
MODEL_NAME = "hf-hub:imageomics/bioclip"

st.set_page_config(page_title="Lithuanian Tree Identifier", page_icon="🌳", layout="centered")


# ---------- cached loaders ----------
@st.cache_resource(show_spinner="Loading models (first run only, ~30 s)...")
def load_models():
    species_clf = joblib.load(APP_DIR / "species_clf.joblib")
    organ_clf = joblib.load(APP_DIR / "organ_clf.joblib")
    with open(APP_DIR / "meta.json", encoding="utf-8") as f:
        meta = json.load(f)
    device = "cuda" if torch.cuda.is_available() else "cpu"
    clip_model, _, preprocess = open_clip.create_model_and_transforms(MODEL_NAME)
    clip_model = clip_model.to(device).eval()
    return species_clf, organ_clf, meta, clip_model, preprocess, device


def embed_image(clip_model, preprocess, device, image_bytes):
    img = Image.open(image_bytes).convert("RGB")
    x = preprocess(img).unsqueeze(0).to(device)
    with torch.no_grad():
        f = clip_model.encode_image(x)
    return torch.nn.functional.normalize(f.float(), dim=-1).cpu().numpy()


# ---------- page ----------
st.title("🌳 Lithuanian Tree Identifier")
st.caption(
    "Upload a photo of a leaf, bark, whole tree, or fruit. "
    "The model guesses the species and the organ type. "
    "28 native Lithuanian species. Trained on iNaturalist photos via GBIF."
)

species_clf, organ_clf, meta, clip_model, preprocess, device = load_models()
classes = meta["classes"]
organs = meta["organs"]
latin_to_lt = meta["latin_to_lithuanian"]
val_acc = meta.get("val_acc")

uploaded = st.file_uploader(
    "Choose an image", type=["jpg", "jpeg", "png", "webp", "bmp"]
)

if uploaded is None:
    st.info("No image yet — upload one above to get a prediction.")
    if val_acc is not None:
        st.caption(f"Model validation accuracy: {val_acc:.1%} (top-1, held-out observers).")
    st.stop()

col_img, col_pred = st.columns([1, 1])

with col_img:
    st.image(uploaded, caption=uploaded.name, use_container_width=True)

with col_pred:
    with st.spinner("Analysing image..."):
        try:
            feat = embed_image(clip_model, preprocess, device, uploaded)
        except Exception as e:
            st.error(f"Could not read the image: {e}")
            st.stop()

        # Species prediction
        sp_proba = species_clf.predict_proba(feat)[0]
        sp_classes = species_clf.classes_

        # Build full-length array in case some species were absent from training
        full = np.zeros(len(classes))
        for idx, p in zip(sp_classes, sp_proba):
            full[idx] = p
        order = np.argsort(-full)

        # Organ prediction
        org_proba = organ_clf.predict_proba(feat)[0]
        org_classes = organ_clf.classes_
        org_full = np.zeros(len(organs))
        for idx, p in zip(org_classes, org_proba):
            org_full[idx] = p
        org_idx = int(org_full.argmax())

    top1 = order[0]
    st.subheader("Prediction")
    st.markdown(
        f"### {latin_to_lt.get(classes[top1], classes[top1])}\n"
        f"*{classes[top1]}* — confidence {full[top1]:.1%}"
    )

    st.markdown("**Top 3 species**")
    for i in order[:3]:
        latin = classes[i]
        lt = latin_to_lt.get(latin, latin)
        st.progress(float(full[i]), text=f"{lt} ({latin}) — {full[i]:.1%}")

    st.markdown("**Detected organ**")
    st.progress(
        float(org_full[org_idx]),
        text=f"{organs[org_idx]} — {org_full[org_idx]:.1%}",
    )

    if organs[org_idx] == "bark":
        st.warning(
            "Bark photos are under-represented in the training data (~500 of 23k images), "
            "so bark predictions are less reliable than leaf or whole-tree ones."
        )
    elif organs[org_idx] == "fruit":
        st.info("Fruit/seed photos often mislead the species model. Cross-check with a leaf photo if possible.")

st.divider()
with st.expander("About this model"):
    st.markdown(
        f"""
- **Backbone:** BioCLIP (imageomics/bioclip), zero-shot image encoder
- **Classifier:** logistic regression on 512-dim embeddings
- **Training data:** ~23,000 iNaturalist research-grade photos from GBIF, 28 Lithuanian tree species
- **Validation:** {val_acc:.1%} top-1 accuracy on held-out observers (not held-out images — this is stricter)
- **Organ classes:** {", ".join(organs)}
- **Limitation:** bark is rare in the dataset. Also, this model only covers 28 species — anything else will still be assigned one of them.
        """
    )
    st.caption(
        "Images used for training are CC0 / CC-BY / CC-BY-NC. "
        "See ATTRIBUTION.csv in the training repository for per-image credits."
    )
