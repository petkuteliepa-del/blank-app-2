# streamlit_app.py
import base64
import json
from pathlib import Path

import joblib
import numpy as np
import streamlit as st
import torch
import open_clip
from PIL import Image

st.set_page_config(page_title="Lietuvos medžių identifikatorius", layout="wide")

try:
    from species_descriptions import SPECIES_DESCRIPTIONS, sp_name, sp_desc, sp_feature
except ImportError:
    st.error("Trūksta failo species_descriptions.py. Įkelkite jį į repozitoriją šalia streamlit_app.py.")
    st.stop()

APP_DIR = Path(__file__).parent
MODEL_NAME = "hf-hub:imageomics/bioclip"
LOGO_PATH = APP_DIR / "logo.png"
CURSOR_PATH = APP_DIR / "cursor.png"

LANG_NAMES = {"lt": "Lietuvių", "en": "English", "de": "Deutsch",
              "fr": "Français", "es": "Español", "uk": "Українська"}

if "lang" not in st.session_state or st.session_state["lang"] not in LANG_NAMES:
    st.session_state["lang"] = "lt"
lang = st.session_state["lang"]

TEXTS = {
    "lt": {
        "title": "Paplitusių Lietuvos sumedėjusių augalų identifikavimo priemonė",
        "subtitle": "Mokymosi priemonė dendrologijos studentams",
        "lang_label": "Kalba", "upload": "Įkelkite nuotrauką", "camera": "Fotografuoti",
        "how": "Kaip ši programėlė veikia?",
        "how_text": (
            "Programa naudoja dirbtinio intelekto modelį **BioCLIP**, kuris nuotrauką "
            "paverčia skaitmeniniu „pirštų atspaudu“. Klasifikatorius, apmokytas su "
            "~23 000 iNaturalist nuotraukų, palygina jūsų nuotrauką su 28 Lietuvos "
            "medžių rūšimis ir išrenka tikimiausią.\n\n"
            "**Kaip naudotis:** įkelkite nuotrauką arba nufotografuokite telefonu ir "
            "palaukite kelių sekundžių. Kairėje – visų 28 rūšių sąrašas su aprašymais."
        ),
        "privacy": "Privatumo politika (BDAR)",
        "privacy_text": (
            "Ši programa **nekaupia ir nesaugo** jūsų nuotraukų. Nuotraukos "
            "apdorojamos tik serverio atmintyje tol, kol pateikiamas atsakymas, ir "
            "iškart ištrinamos.\n\nJei turite klausimų dėl duomenų tvarkymo pagal "
            "**BDAR** (Reglamentas 2016/679), susisiekite su projekto autoriumi."
        ),
        "species_header": "Įrankio atpažįstamų rūšių sąrašas",
        "species_hint": "Spustelėkite rūšį, kad pamatytumėte aprašymą.",
        "others": "Kitos galimos rūšys", "analyzing": "Tikrinu...",
        "no_image": "Įkelkite nuotrauką – ir kartu išsiaiškinsime, kas čia auga.",
        "features_label": "Kodėl manome, kad tai ši rūšis",
        "why_other": "Kodėl ji taip pat galima",
        "disclaimer": ("Tai dirbtinio intelekto įrankis – jis gali klysti. "
                       "Rekomenduojama rūšį patikrinti su dėstytoju."),
        "footer": "Tai studentų projektas, sukurtas dirbtinio intelekto kurso metu.",
    },
    "en": {
        "title": "Identification Tool for Common Lithuanian Woody Plants",
        "subtitle": "A learning tool for dendrology students",
        "lang_label": "Language", "upload": "Upload a photo", "camera": "Take a photo",
        "how": "How does this app work?",
        "how_text": ("The app uses **BioCLIP** to turn your photo into a numeric "
                     "fingerprint. A classifier trained on ~23,000 iNaturalist photos "
                     "compares it against 28 Lithuanian tree species.\n\n"
                     "**How to use:** upload a photo (or snap one with your phone) "
                     "and wait a few seconds."),
        "privacy": "Privacy policy (GDPR)",
        "privacy_text": ("This app **does not store** your photos. Images are "
                         "processed only in server memory during prediction.\n\n"
                         "For questions under **GDPR** (Regulation 2016/679), "
                         "contact the project author."),
        "species_header": "List of species the tool recognises",
        "species_hint": "Click a species to see its description.",
        "others": "Other possible species", "analyzing": "Checking...",
        "no_image": "Upload a photo – let's figure out together what grows here.",
        "features_label": "Why we think it's this species",
        "why_other": "Why it's also possible",
        "disclaimer": ("This is an AI tool and it can be wrong. "
                       "Please check the species with your professor."),
        "footer": "This is a student project made for an AI class.",
    },
    "de": {
        "title": "Bestimmungshilfe für verbreitete litauische Gehölze",
        "subtitle": "Ein Lernwerkzeug für Dendrologie-Studierende",
        "lang_label": "Sprache", "upload": "Foto hochladen", "camera": "Foto aufnehmen",
        "how": "Wie funktioniert diese App?",
        "how_text": ("Die App nutzt **BioCLIP**, um dein Foto in einen numerischen "
                     "Fingerabdruck umzuwandeln. Ein Klassifikator, trainiert mit "
                     "~23.000 iNaturalist-Fotos, vergleicht es mit 28 Baumarten."),
        "privacy": "Datenschutz (DSGVO)",
        "privacy_text": ("Diese App **speichert keine** Fotos. Bilder werden nur "
                         "im Server-Speicher während der Vorhersage verarbeitet.\n\n"
                         "Bei Fragen nach **DSGVO** kontaktiere den Projektautor."),
        "species_header": "Liste der erkannten Arten",
        "species_hint": "Klicke auf eine Art, um die Beschreibung zu sehen.",
        "others": "Andere mögliche Arten", "analyzing": "Prüfe...",
        "no_image": "Lade ein Foto hoch – finden wir heraus, was hier wächst.",
        "features_label": "Warum wir diese Art vermuten",
        "why_other": "Warum sie ebenfalls möglich ist",
        "disclaimer": "Dies ist ein KI-Werkzeug und kann Fehler machen. "
                      "Bitte überprüfe die Art mit deinem Professor.",
        "footer": "Dies ist ein Studierendenprojekt für einen KI-Kurs.",
    },
    "fr": {
        "title": "Outil d'identification des plantes ligneuses lituaniennes communes",
        "subtitle": "Un outil pédagogique pour les étudiants en dendrologie",
        "lang_label": "Langue", "upload": "Téléverser une photo",
        "camera": "Prendre une photo",
        "how": "Comment fonctionne cette application ?",
        "how_text": ("L'application utilise **BioCLIP** pour transformer votre photo "
                     "en une empreinte numérique. Un classificateur entraîné sur "
                     "~23 000 photos iNaturalist la compare à 28 espèces."),
        "privacy": "Politique de confidentialité (RGPD)",
        "privacy_text": ("Cette application **ne stocke pas** vos photos. Les images "
                         "sont traitées uniquement en mémoire du serveur.\n\n"
                         "Pour toute question au titre du **RGPD**, contactez l'auteur."),
        "species_header": "Liste des espèces reconnues",
        "species_hint": "Cliquez sur une espèce pour voir sa description.",
        "others": "Autres espèces possibles", "analyzing": "Vérification...",
        "no_image": "Téléversez une photo – découvrons ensemble ce qui pousse ici.",
        "features_label": "Pourquoi nous pensons qu'il s'agit de cette espèce",
        "why_other": "Pourquoi elle est aussi possible",
        "disclaimer": "Cet outil d'IA peut se tromper. "
                      "Veuillez vérifier l'espèce avec votre professeur.",
        "footer": "Projet étudiant réalisé pour un cours d'IA.",
    },
    "es": {
        "title": "Herramienta de identificación de plantas leñosas lituanas comunes",
        "subtitle": "Una herramienta de aprendizaje para estudiantes de dendrología",
        "lang_label": "Idioma", "upload": "Subir una foto", "camera": "Tomar una foto",
        "how": "¿Cómo funciona esta aplicación?",
        "how_text": ("La aplicación usa **BioCLIP** para convertir tu foto en una "
                     "huella numérica. Un clasificador entrenado con ~23 000 fotos de "
                     "iNaturalist la compara con 28 especies."),
        "privacy": "Política de privacidad (RGPD)",
        "privacy_text": ("Esta aplicación **no almacena** tus fotos. Las imágenes se "
                         "procesan solo en la memoria del servidor.\n\nPara preguntas "
                         "según el **RGPD**, contacta con el autor."),
        "species_header": "Lista de especies que reconoce la herramienta",
        "species_hint": "Haz clic en una especie para ver su descripción.",
        "others": "Otras especies posibles", "analyzing": "Comprobando...",
        "no_image": "Sube una foto y descubramos juntos qué crece aquí.",
        "features_label": "Por qué creemos que es esta especie",
        "why_other": "Por qué también es posible",
        "disclaimer": "Esta herramienta de IA puede equivocarse. "
                      "Verifica la especie con tu profesor.",
        "footer": "Proyecto estudiantil realizado para un curso de IA.",
    },
    "uk": {
        "title": "Інструмент для визначення поширених литовських деревних рослин",
        "subtitle": "Навчальний інструмент для студентів-дендрологів",
        "lang_label": "Мова", "upload": "Завантажити фото", "camera": "Зробити фото",
        "how": "Як працює цей застосунок?",
        "how_text": ("Застосунок використовує **BioCLIP**, щоб перетворити вашу "
                     "фотографію на числовий відбиток. Класифікатор, навчений на "
                     "~23 000 фотографій iNaturalist, порівнює її з 28 видами."),
        "privacy": "Політика конфіденційності (GDPR)",
        "privacy_text": ("Цей застосунок **не зберігає** ваші фотографії. Зображення "
                         "обробляються лише в пам'яті сервера.\n\nЗ питань "
                         "відповідно до **GDPR** звертайтеся до автора."),
        "species_header": "Список видів, які розпізнає інструмент",
        "species_hint": "Натисніть на вид, щоб побачити опис.",
        "others": "Інші можливі види", "analyzing": "Перевіряю...",
        "no_image": "Завантажте фото – і разом з'ясуємо, що тут росте.",
        "features_label": "Чому ми вважаємо, що це саме цей вид",
        "why_other": "Чому він також можливий",
        "disclaimer": "Це інструмент ШІ, і він може помилятися. "
                      "Перевірте вид разом із викладачем.",
        "footer": "Студентський проєкт, створений для курсу зі штучного інтелекту.",
    },
}

t = TEXTS[lang]

def _load_cursor_b64(path):
    if not path.exists():
        return ""
    try:
        if path.stat().st_size > 500_000:
            return ""
        with Image.open(path) as im:
            im.verify()
        return base64.b64encode(path.read_bytes()).decode()
    except Exception:
        return ""

cursor_b64 = _load_cursor_b64(CURSOR_PATH)
if not cursor_b64:
    cursor_b64 = _load_cursor_b64(LOGO_PATH)

cursor_css = ""
if cursor_b64:
    cursor_css = (
        "* { cursor: url('data:image/png;base64," + cursor_b64 + "') 16 16, auto !important; }"
    )

st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    html, body, .stApp, .stMarkdown, .stText, .stCaption,
    .stTabs, .stInfo, .stWarning, h1, h2, h3, h4, h5, h6, p, label, button,
    input, div[role="button"] {{
        font-family: 'Inter', sans-serif !important;
    }}
    {cursor_css}

    .block-container {{
        padding-top: 5rem !important;
        padding-bottom: 1rem !important;
        padding-left: 2.5rem !important;
        padding-right: 2.5rem !important;
    }}
    [data-testid="stHeader"] {{ background-color: transparent !important; }}
    [data-testid="stToolbar"] {{ display: none !important; }}
    [data-testid="stDecoration"] {{ display: none !important; }}

    .stApp {{ background-color: #F4F6F1 !important; color: #2B2B2B; }}
    [data-testid="stSidebar"] {{ background-color: #E8EDE3 !important; }}
    h1, h2, h3, h4, h5 {{ color: #1F3B2C !important; font-weight: 700; letter-spacing: -0.015em; }}
    h1 {{ font-size: 3rem !important; line-height: 1.1 !important; }}
    p, .stMarkdown, label {{ color: #2E2E2E; }}

    /* ===== Unified controls (selectbox + 2 popovers) ===== */
    /* Each control row gets a 14px bottom margin so the three are evenly spaced. */
    div[data-testid="stSelectbox"],
    div[data-testid="stPopover"] {{
        width: 100% !important;
        margin: 0 0 14px 0 !important;
    }}

    /* Language selectbox */
    div[data-testid="stSelectbox"] > div,
    div[data-testid="stSelectbox"] div[data-baseweb="select"],
    div[data-testid="stSelectbox"] div[data-baseweb="select"] > div {{
        width: 100% !important;
        min-width: 100% !important;
        height: 56px !important;
        min-height: 56px !important;
        border-radius: 28px !important;
        box-sizing: border-box !important;
    }}
    div[data-testid="stSelectbox"] div[data-baseweb="select"] > div {{
        background-color: #FFFFFF !important;
        border: 1px solid #C8D5BF !important;
        padding: 0 1.15rem !important;
        display: flex !important;
        align-items: center !important;
        font-weight: 600 !important;
        color: #1F3B2C !important;
    }}
    div[data-testid="stSelectbox"] label {{
        font-weight: 600 !important;
        color: #1F3B2C !important;
        font-size: 0.85rem !important;
        margin-bottom: 0.3rem !important;
    }}

    /* Popovers: strip the wrapper, keep ONE border on the button */
    div[data-testid="stPopover"] > div {{
        width: 100% !important;
        border: none !important;
        background: transparent !important;
        padding: 0 !important;
        border-radius: 0 !important;
        box-shadow: none !important;
    }}
    div[data-testid="stPopover"] button {{
        width: 100% !important;
        height: 56px !important;
        min-height: 56px !important;
        border-radius: 28px !important;
        background-color: #FFFFFF !important;
        border: 1px solid #C8D5BF !important;
        color: #1F3B2C !important;
        font-weight: 600 !important;
        padding: 0 1.15rem !important;
        display: inline-flex !important;
        align-items: center !important;
        justify-content: center !important;
        box-sizing: border-box !important;
        box-shadow: none !important;
    }}
    div[data-testid="stPopover"] button:hover {{
        background-color: #DEE7D8 !important;
        border-color: #3E8E5A !important;
        color: #1F3B2C !important;
    }}

    .stButton > button {{
        border-radius: 26px !important;
        background-color: #3E8E5A !important;
        color: #FFFFFF !important;
        border: 1px solid #347A4C !important;
        font-weight: 600 !important;
        padding: 0.55rem 1.1rem !important;
    }}
    .stButton > button:hover {{
        background-color: #2F7548 !important;
        border-color: #2A6B40 !important;
        color: #FFFFFF !important;
    }}

    /* Sidebar species expanders: one border only */
    [data-testid="stExpander"] {{
        border: none !important;
        background: transparent !important;
        box-shadow: none !important;
        border-radius: 0 !important;
        padding: 0 !important;
        margin-bottom: 0.35rem !important;
    }}
    [data-testid="stExpander"] details {{
        border: none !important;
        background: transparent !important;
        box-shadow: none !important;
        border-radius: 0 !important;
        padding: 0 !important;
    }}
    [data-testid="stExpander"] details summary {{
        border-radius: 20px !important;
        background-color: #DEE7D8 !important;
        color: #1F3B2C !important;
        font-weight: 700 !important;
        border: 1px solid #C8D5BF !important;
        padding: 0.7rem 1rem !important;
        box-shadow: none !important;
        outline: none !important;
    }}
    [data-testid="stExpander"] details[open] summary {{
        background-color: #D2DECB !important;
        border-color: #3E8E5A !important;
    }}
    [data-testid="stExpander"] details > div {{
        border: none !important;
        background: transparent !important;
        padding-left: 0.5rem !important;
        padding-right: 0.5rem !important;
    }}

    [data-testid="stFileUploaderDropzone"],
    [data-testid="stFileUploader"] section {{
        min-height: 260px !important;
        border-radius: 22px !important;
        background-color: #FFFFFF !important;
        border: 2px dashed #3E8E5A !important;
        padding: 2.4rem !important;
    }}
    [data-testid="stFileUploader"] section button {{
        border-radius: 26px !important;
        background-color: #3E8E5A !important;
        color: #FFFFFF !important;
        border: none !important;
        padding: 0.7rem 1.6rem !important;
        font-weight: 600 !important;
    }}
    [data-testid="stCameraInput"] {{ border-radius: 22px !important; }}
    .small-grey {{ color: #5A5A5A; font-size: 0.85rem; line-height: 1.4; }}
    .footer-grey {{ color: #6B6B6B; font-size: 0.75rem; text-align: center;
        padding: 2.5rem 0 1rem 0; }}
    .feature-box {{
        background-color: #FFFFFF; border-left: 5px solid #3E8E5A;
        border-radius: 14px; padding: 1rem 1.25rem; margin: 1rem 0;
        color: #2E2E2E; font-size: 0.95rem; line-height: 1.6;
    }}
    .feature-box .feature-label {{ font-weight: 700; color: #1F3B2C;
        margin-bottom: 0.4rem; font-size: 0.98rem; }}
    .alt-species {{ background-color: #EDF2E9; border-radius: 14px;
        padding: 0.85rem 1.1rem; margin-bottom: 0.6rem; border: 1px solid #D2DECB; }}
    .alt-species .alt-name {{ font-weight: 700; color: #1F3B2C; font-size: 1rem; }}
    .alt-species .alt-conf {{ color: #3E8E5A; font-weight: 600; margin-left: 0.4rem; }}
    .alt-species .alt-reason {{ color: #555; font-size: 0.88rem;
        margin-top: 0.3rem; line-height: 1.45; }}
    .top-pred-name {{ font-size: 2rem; font-weight: 800; color: #1F3B2C;
        margin-bottom: 0.15rem; line-height: 1.15; }}
    .top-pred-conf {{ font-size: 1.1rem; color: #3E8E5A; font-weight: 700;
        margin-bottom: 0.2rem; }}
    .top-pred-latin {{ color: #666; font-style: italic; font-size: 0.95rem;
        margin-bottom: 0.5rem; }}
    [data-testid="stTabs"] button[role="tab"] {{ border-radius: 14px 14px 0 0; color: #1F3B2C; }}
    [data-testid="stTabs"] button[role="tab"][aria-selected="true"] {{
        background-color: #DEE7D8; border-bottom-color: #3E8E5A; }}
    #MainMenu, footer {{ visibility: hidden; }}
    </style>
    """,
    unsafe_allow_html=True,
)


@st.cache_resource(show_spinner="Loading models...")
def load_models():
    species_clf = joblib.load(APP_DIR / "species_clf.joblib")
    with open(APP_DIR / "meta.json", encoding="utf-8") as f:
        meta = json.load(f)
    device = "cuda" if torch.cuda.is_available() else "cpu"
    clip_model, _, preprocess = open_clip.create_model_and_transforms(MODEL_NAME)
    clip_model = clip_model.to(device).eval()
    return species_clf, meta, clip_model, preprocess, device


def embed_image(clip_model, preprocess, device, image_source):
    img = Image.open(image_source).convert("RGB")
    x = preprocess(img).unsqueeze(0).to(device)
    with torch.no_grad():
        f = clip_model.encode_image(x)
    return torch.nn.functional.normalize(f.float(), dim=-1).cpu().numpy()


try:
    species_clf, meta, clip_model, preprocess, device = load_models()
    classes = meta["classes"]
except Exception as e:
    st.error(f"Nepavyko įkelti modelio: {e}")
    st.stop()


def _lang_changed():
    new = st.session_state.get("lang_selector_ui")
    if new in LANG_NAMES:
        st.session_state["lang"] = new


with st.sidebar:
    st.subheader(t["species_header"])
    st.caption(t["species_hint"])
    for latin in sorted(SPECIES_DESCRIPTIONS.keys(), key=lambda k: sp_name(k, lang).lower()):
        with st.expander(f"{sp_name(latin, lang)} ({latin})"):
            st.write(sp_desc(latin, lang))

col_main, col_ctrl = st.columns([7, 3], vertical_alignment="center")

with col_main:
    if LOGO_PATH.exists():
        try:
            logo_img = Image.open(LOGO_PATH)
            logo_img.load()
            st.image(logo_img, width=350)
        except Exception:
            pass
    st.markdown(f"<h1 style='margin:0.4rem 0 0.15rem 0;'>{t['title']}</h1>",
                unsafe_allow_html=True)
    st.markdown(f"<div class='small-grey'>{t['subtitle']}</div>",
                unsafe_allow_html=True)

with col_ctrl:
    langs = list(LANG_NAMES.keys())
    cur_idx = langs.index(lang) if lang in langs else 0
    st.selectbox(
        t["lang_label"],
        options=langs,
        format_func=lambda k: LANG_NAMES[k],
        index=cur_idx,
        key="lang_selector_ui",
        on_change=_lang_changed,
    )
    with st.popover(t["how"]):
        st.markdown(t["how_text"])
    with st.popover(t["privacy"]):
        st.markdown(t["privacy_text"])

st.divider()

tab_upload, tab_camera = st.tabs([t["upload"], t["camera"]])
with tab_upload:
    uploaded = st.file_uploader(
        t["upload"], type=["jpg", "jpeg", "png", "webp", "bmp"],
        label_visibility="collapsed", key="uploader",
    )
with tab_camera:
    camera_shot = st.camera_input(t["camera"], label_visibility="collapsed", key="camera")

image_source = uploaded if uploaded is not None else camera_shot

if image_source is None:
    st.info(t["no_image"])
else:
    col_img, col_pred = st.columns([1, 1.2])
    with col_img:
        st.image(image_source, use_container_width=True)
    with col_pred:
        with st.spinner(t["analyzing"]):
            try:
                feat = embed_image(clip_model, preprocess, device, image_source)
            except Exception as e:
                st.error(f"Could not read the image: {e}")
                st.stop()
            sp_proba = species_clf.predict_proba(feat)[0]
            sp_classes = species_clf.classes_
            full = np.zeros(len(classes))
            for idx, p in zip(sp_classes, sp_proba):
                full[idx] = p
            order = np.argsort(-full)

        top1 = order[0]
        top1_latin = classes[top1]
        top1_conf = float(full[top1])

        st.markdown(
            f"<div class='top-pred-name'>{sp_name(top1_latin, lang)}</div>"
            f"<div class='top-pred-conf'>({top1_conf:.1%})</div>"
            f"<div class='top-pred-latin'>{top1_latin}</div>",
            unsafe_allow_html=True,
        )

        features = sp_feature(top1_latin, lang)
        if features:
            st.markdown(
                f"<div class='feature-box'>"
                f"<div class='feature-label'>{t['features_label']}</div>"
                f"{features}</div>",
                unsafe_allow_html=True,
            )

        if top1_conf < 0.9995:
            alts = [i for i in order[1:4] if full[i] > 0.005]
            if alts:
                st.markdown(f"**{t['others']}**")
                for i in alts:
                    alt_latin = classes[i]
                    st.markdown(
                        f"<div class='alt-species'>"
                        f"<span class='alt-name'>{sp_name(alt_latin, lang)} ({alt_latin})</span>"
                        f"<span class='alt-conf'>{float(full[i]):.1%}</span>"
                        f"<div class='alt-reason'>{t['why_other']}: "
                        f"{sp_feature(alt_latin, lang)}</div></div>",
                        unsafe_allow_html=True,
                    )

        st.markdown(f"<div class='small-grey' style='margin-top:1rem;'>"
                    f"{t['disclaimer']}</div>", unsafe_allow_html=True)

st.markdown(f"<div class='footer-grey'>{t['footer']}</div>", unsafe_allow_html=True)
