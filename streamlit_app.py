# streamlit_app.py
import json
from pathlib import Path

import joblib
import numpy as np
import streamlit as st
import torch
import open_clip
from PIL import Image

APP_DIR = Path(__file__).parent
MODEL_NAME = "hf-hub:imageomics/bioclip"

st.set_page_config(
    page_title="Lietuvos medžių identifikatorius",
    page_icon="🌰",
    layout="wide",
)

# ---------- styling ----------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    html, body, .stApp, .stMarkdown, .stText, .stCaption,
    .stSelectbox, .stButton > button, .stTabs, .stInfo,
    h1, h2, h3, h4, h5, h6, p, label {
        font-family: 'Inter', sans-serif !important;
    }
    .stApp { background-color: #9FC79F !important; }
    [data-testid="stSidebar"] { background-color: #8FB98F !important; }
    [data-testid="stHeader"] { background-color: rgba(0,0,0,0) !important; }
    .block-container { padding-top: 1.5rem; }

    h1, h2, h3, h4 { color: #1b3a1b; }

    .small-grey { color: #4d4d4d; font-size: 0.85rem; line-height: 1.35; }
    .footer-grey {
        color: #666666; font-size: 0.75rem; text-align: center;
        padding-top: 2.5rem; padding-bottom: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- languages ----------
LANG_NAMES = {
    "lt": "Lietuvių",
    "en": "English",
    "de": "Deutsch",
    "fr": "Français",
    "es": "Español",
    "uk": "Українська",
}

TEXTS = {
    "lt": {
        "lang_label": "Kalba",
        "upload": "Įkelkite nuotrauką",
        "camera": "Fotografuoti",
        "how": "Kaip tai veikia?",
        "how_text": (
            "Programa naudoja dirbtinio intelekto modelį **BioCLIP**, kuris nuotrauką "
            "paverčia skaitmeniniu „pirštų atspaudu“ (įterpiniu). Tada logistinės "
            "regresijos klasifikatorius, apmokytas su ~23 000 iNaturalist nuotraukų, "
            "palygina jūsų nuotrauką su 28 Lietuvos medžių rūšimis ir išrenka "
            "tikimiausią. Papildomai nustatoma, ar nuotraukoje matomas lapas, žievė, "
            "visas medis ar vaisius.\n\n"
            "**Kaip naudotis:** įkelkite nuotrauką (arba nufotografuokite telefonu) ir "
            "palaukite kelių sekundžių. Kairėje pusėje galite naršyti visas 28 rūšis ir "
            "skaityti jų trumpus aprašymus."
        ),
        "privacy": "Privatumo politika (BDAR)",
        "privacy_text": (
            "Ši programa **nekaupia ir nesaugo** jūsų nuotraukų. Nuotraukos "
            "apdorojamos tik serverio atmintyje tol, kol pateikiamas atsakymas, ir "
            "iškart ištrinamos. Nesurenkame asmens duomenų ir nenaudojame slapukų "
            "rinkodaros tikslams.\n\n"
            "Jei turite klausimų dėl duomenų tvarkymo pagal **BDAR** "
            "(Reglamentas 2016/679), susisiekite su projekto autoriumi. "
            "Duomenų valdytojas – projekto rengėjas (studentas)."
        ),
        "species_header": "Atpažįstamos rūšys",
        "species_hint": "Spustelėkite rūšį, kad pamatytumėte trumpą aprašymą.",
        "prediction": "Prognozė",
        "top3": "Tikimiausios rūšys",
        "organ": "Nustatytas augalo organas",
        "confidence": "pasitikėjimas",
        "analyzing": "Analizuojama...",
        "no_image": "Įkelkite nuotrauką, kad gautumėte prognozę.",
        "pick_species": "Pasirinkite rūšį iš sąrašo, kad pamatytumėte aprašymą.",
        "disclaimer": (
            "Tai dirbtinio intelekto įrankis – jis gali klysti. "
            "Rekomenduojama rūšį patikrinti su dėstytoju."
        ),
        "footer": "Tai studentų projektas, sukurtas dirbtinio intelekto kurso metu.",
    },
    "en": {
        "lang_label": "Language",
        "upload": "Upload a photo",
        "camera": "Take a photo",
        "how": "How does this app work?",
        "how_text": (
            "The app uses the **BioCLIP** AI model to turn your photo into a numeric "
            "“fingerprint” (embedding). A logistic-regression classifier, trained on "
            "~23,000 iNaturalist photos, then compares your photo against 28 Lithuanian "
            "tree species and picks the most likely one. It also detects whether the "
            "photo shows a leaf, bark, the whole tree, or fruit.\n\n"
            "**How to use it:** upload a photo (or snap one with your phone) and wait a "
            "few seconds. On the left you can browse all 28 species and read short "
            "descriptions."
        ),
        "privacy": "Privacy policy (GDPR)",
        "privacy_text": (
            "This app does **not store** your photos. Images are processed in server "
            "memory only while a prediction is being made, and are deleted immediately "
            "after. We do not collect personal data or use marketing cookies.\n\n"
            "For questions about data processing under **GDPR** (Regulation 2016/679), "
            "contact the project author. Data controller: the project author (student)."
        ),
        "species_header": "Recognised species",
        "species_hint": "Click a species to see a short description.",
        "prediction": "Prediction",
        "top3": "Most likely species",
        "organ": "Detected plant organ",
        "confidence": "confidence",
        "analyzing": "Analysing...",
        "no_image": "Upload a photo to get a prediction.",
        "pick_species": "Pick a species from the list to see its description.",
        "disclaimer": (
            "This is an AI tool and it can be wrong. "
            "Please check the species with your professor."
        ),
        "footer": "This is a student project made for an AI class.",
    },
    "de": {
        "lang_label": "Sprache",
        "upload": "Foto hochladen",
        "camera": "Foto aufnehmen",
        "how": "Wie funktioniert diese App?",
        "how_text": (
            "Die App nutzt das KI-Modell **BioCLIP**, um dein Foto in einen numerischen "
            "„Fingerabdruck“ (Embedding) umzuwandeln. Ein logistischer Regressions-"
            "Klassifikator, trainiert mit ~23.000 iNaturalist-Fotos, vergleicht dein Foto "
            "mit 28 litauischen Baumarten und wählt die wahrscheinlichste. Zusätzlich "
            "erkennt er, ob das Foto ein Blatt, Rinde, den ganzen Baum oder Früchte zeigt."
        ),
        "privacy": "Datenschutz (DSGVO)",
        "privacy_text": (
            "Diese App **speichert keine** Fotos. Bilder werden nur im Server-Speicher "
            "verarbeitet, während eine Vorhersage erstellt wird, und sofort danach "
            "gelöscht. Wir sammeln keine personenbezogenen Daten und verwenden keine "
            "Marketing-Cookies.\n\n"
            "Bei Fragen zur Datenverarbeitung nach **DSGVO** (Verordnung 2016/679) "
            "kontaktiere bitte den Projektautor (Studierender)."
        ),
        "species_header": "Erkannte Arten",
        "species_hint": "Klicke auf eine Art, um eine kurze Beschreibung zu sehen.",
        "prediction": "Vorhersage",
        "top3": "Wahrscheinlichste Arten",
        "organ": "Erkanntes Pflanzenorgan",
        "confidence": "Konfidenz",
        "analyzing": "Analyse läuft...",
        "no_image": "Lade ein Foto hoch, um eine Vorhersage zu erhalten.",
        "pick_species": "Wähle eine Art aus der Liste, um die Beschreibung zu sehen.",
        "disclaimer": (
            "Dies ist ein KI-Werkzeug und kann Fehler machen. "
            "Bitte überprüfe die Art mit deinem Professor."
        ),
        "footer": "Dies ist ein Studierendenprojekt für einen KI-Kurs.",
    },
    "fr": {
        "lang_label": "Langue",
        "upload": "Téléverser une photo",
        "camera": "Prendre une photo",
        "how": "Comment fonctionne cette application ?",
        "how_text": (
            "L'application utilise le modèle d'IA **BioCLIP** pour transformer votre "
            "photo en une « empreinte » numérique (embedding). Un classificateur de "
            "régression logistique, entraîné sur ~23 000 photos iNaturalist, compare "
            "ensuite votre photo à 28 espèces d'arbres lituaniens et choisit la plus "
            "probable. Il détecte aussi si la photo montre une feuille, de l'écorce, "
            "l'arbre entier ou un fruit."
        ),
        "privacy": "Politique de confidentialité (RGPD)",
        "privacy_text": (
            "Cette application **ne stocke pas** vos photos. Les images sont traitées "
            "uniquement en mémoire du serveur pendant la prédiction, puis supprimées "
            "immédiatement. Nous ne collectons aucune donnée personnelle et n'utilisons "
            "pas de cookies marketing.\n\n"
            "Pour toute question sur le traitement des données au titre du **RGPD** "
            "(Règlement 2016/679), contactez l'auteur du projet (étudiant)."
        ),
        "species_header": "Espèces reconnues",
        "species_hint": "Cliquez sur une espèce pour voir une courte description.",
        "prediction": "Prédiction",
        "top3": "Espèces les plus probables",
        "organ": "Organe détecté",
        "confidence": "confiance",
        "analyzing": "Analyse en cours...",
        "no_image": "Téléversez une photo pour obtenir une prédiction.",
        "pick_species": "Choisissez une espèce dans la liste pour voir sa description.",
        "disclaimer": (
            "Cet outil d'IA peut se tromper. "
            "Veuillez vérifier l'espèce avec votre professeur."
        ),
        "footer": "Projet étudiant réalisé pour un cours d'IA.",
    },
    "es": {
        "lang_label": "Idioma",
        "upload": "Subir una foto",
        "camera": "Tomar una foto",
        "how": "¿Cómo funciona esta aplicación?",
        "how_text": (
            "La aplicación usa el modelo de IA **BioCLIP** para convertir tu foto en una "
            "«huella» numérica (embedding). Un clasificador de regresión logística, "
            "entrenado con ~23 000 fotos de iNaturalist, compara tu foto con 28 especies "
            "de árboles lituanos y elige la más probable. También detecta si la foto "
            "muestra una hoja, corteza, el árbol completo o un fruto."
        ),
        "privacy": "Política de privacidad (RGPD)",
        "privacy_text": (
            "Esta aplicación **no almacena** tus fotos. Las imágenes se procesan solo en "
            "la memoria del servidor mientras se genera la predicción y se eliminan "
            "inmediatamente después. No recopilamos datos personales ni usamos cookies "
            "de marketing.\n\n"
            "Para preguntas sobre el tratamiento de datos según el **RGPD** "
            "(Reglamento 2016/679), contacta con el autor del proyecto (estudiante)."
        ),
        "species_header": "Especies reconocidas",
        "species_hint": "Haz clic en una especie para ver una breve descripción.",
        "prediction": "Predicción",
        "top3": "Especies más probables",
        "organ": "Órgano detectado",
        "confidence": "confianza",
        "analyzing": "Analizando...",
        "no_image": "Sube una foto para obtener una predicción.",
        "pick_species": "Elige una especie de la lista para ver su descripción.",
        "disclaimer": (
            "Esta herramienta de IA puede equivocarse. "
            "Verifica la especie con tu profesor."
        ),
        "footer": "Proyecto estudiantil realizado para un curso de IA.",
    },
    "uk": {
        "lang_label": "Мова",
        "upload": "Завантажити фото",
        "camera": "Зробити фото",
        "how": "Як працює цей застосунок?",
        "how_text": (
            "Застосунок використовує модель ШІ **BioCLIP**, яка перетворює вашу "
            "фотографію на числовий «відбиток» (ембединг). Потім класифікатор "
            "логістичної регресії, навчений на ~23 000 фотографій iNaturalist, "
            "порівнює ваше фото з 28 видами литовських дерев і вибирає найімовірніший. "
            "Додатково визначається, що на фото: листок, кора, усе дерево або плід.\n\n"
            "**Як користуватися:** завантажте фото (або сфотографуйте телефоном) і "
            "зачекайте кілька секунд. Ліворуч ви можете переглянути всі 28 видів і "
            "прочитати їхні короткі описи."
        ),
        "privacy": "Політика конфіденційності (GDPR)",
        "privacy_text": (
            "Цей застосунок **не зберігає** ваші фотографії. Зображення обробляються "
            "лише в пам'яті сервера, поки формується відповідь, і одразу видаляються. "
            "Ми не збираємо персональні дані й не використовуємо маркетингові cookie.\n\n"
            "З питань обробки даних відповідно до **GDPR** (Регламент 2016/679) "
            "звертайтеся до автора проєкту (студента)."
        ),
        "species_header": "Розпізнавані види",
        "species_hint": "Натисніть на вид, щоб побачити короткий опис.",
        "prediction": "Прогноз",
        "top3": "Найімовірніші види",
        "organ": "Визначений орган рослини",
        "confidence": "впевненість",
        "analyzing": "Аналіз...",
        "no_image": "Завантажте фото, щоб отримати прогноз.",
        "pick_species": "Виберіть вид зі списку, щоб побачити опис.",
        "disclaimer": (
            "Це інструмент ШІ, і він може помилятися. "
            "Будь ласка, перевірте вид разом із викладачем."
        ),
        "footer": "Студентський проєкт, створений для курсу зі штучного інтелекту.",
    },
}

# ---------- species descriptions (Lithuanian) ----------
SPECIES_DESCRIPTIONS = {
    "Acer platanoides": "Lapai plačiai skiltuoti (5 skiltys), rudenį ryškiai geltoni. Jauna žievė lygi, vėliau išilgai vagota. Vaisiai – sparnuoti sparnavaisiai poromis.",
    "Alnus glutinosa": "Lapai atvirkščiai kiaušiniški, su įkirptu viršūniu, blizgūs. Žievė tamsi, giliai sueižėjusi. Auga šlapiose vietose, dažnai prie vandens.",
    "Alnus incana": "Lapai smailūs, dantyti, apatinė pusė pilkai plaukuota. Žievė lygi, šviesiai pilka. Dažnas pakelėse ir upių slėniuose.",
    "Betula pendula": "Balta žievė su juodomis juostelėmis, jaunos šakelės karpotos. Lapai rombiški, smailūs, dvigubai dantyti.",
    "Betula pubescens": "Labai panašus į karpotąjį beržą, bet jaunos šakelės ir lapai plaukuoti, lapai platesni, šiek tiek širdiški.",
    "Carpinus betulus": "Lapai ovalūs, dantyti, su ryškiomis gyslomis. Žievė lygi, pilka, lyg „raumenų“. Vaisiai – smulkūs riešutėliai su lapeliu-kapučiu.",
    "Fagus sylvatica": "Lapai blizgūs, elipsiški, lygiais kraštais. Žievė lygi, pilka. Riešutai – trikampiai buku­kai, dygliuotuose gaubtuose.",
    "Fraxinus excelsior": "Lapai sudėtiniai (5–9 lapeliai), priešiniai. Žiemą ryškūs juodi pumpurai. Vaisiai – sparnuoti, sukabinti kekėmis.",
    "Juniperus communis": "Krūmas arba mažas medis. Spygliai dygliuoti, 1–2 cm, išsidėstę po tris. Uogos melsvai juodos, apvalios.",
    "Larix decidua": "Vienintelis Lietuvoje spyglius numetantis spygliuotis – rudenį spygliuoja geltonai. Kankorėžiai smulkūs, kiaušiniški, 2–4 cm.",
    "Malus sylvestris": "Nedidelis medis su dygliuotomis šakelėmis. Lapai ovalūs, dantyti. Vaisiai – smulkūs, rūgštūs obuoliai.",
    "Picea abies": "Siaurai piramidinis kūgis. Spygliai tamsiai žali, 1–2,5 cm. Kankorėžiai ilgi, cilindriški, kabantys žemyn.",
    "Pinus sylvestris": "Spygliai 4–7 cm, išsidėstę po du. Viršutinė kamieno žievė oranžiškai rausva, plokštelėmis. Kankorėžiai smulkūs, kūgiški.",
    "Populus nigra": "Storas kamienas su tamsia, giliai sueižėjusia žieve. Lapai trikampiški arba rombiški, smailūs.",
    "Populus tremula": "Lapai apvalūs, ilgais koteliais – virpa net lengvame vėjyje. Žievė lygi, pilkai žalia, su rombiškomis „akimis“.",
    "Prunus padus": "Lapai pailgi, dantyti. Pavasarį – kvapnios baltos žiedų kekės. Vaisiai – smulkios juodos uogos.",
    "Pyrus pyraster": "Panaši į miškinę obelį, bet vaisiai kieti, smulkūs, kriaušės formos. Šakelės su dygliais.",
    "Quercus petraea": "Panašus į paprastąjį ąžuolą, bet lapai su aiškiu koteliu, giles be kotelio. Lapų skiltys lygesnės.",
    "Quercus robur": "Lapai su apvaliomis skiltimis, beveik bekociai. Žievė giliai sueižėjusi. Gilės su dubenėliu ant kotelio.",
    "Salix alba": "Lapai pailgi, sidabriškai žali (ypač apatinė pusė). Šakelės lanksčios, geltonos arba rausvos.",
    "Salix caprea": "Stambūs, platūs, apvalūs lapai su raukšlėtu paviršiumi. Pavasarį – dideli, pilki „kačiukai“ (žiedynai).",
    "Salix fragilis": "Labai panašus į baltąjį gluosnį, bet šakelės lengvai lūžta. Lapai blizgūs, plonesni.",
    "Sorbus aucuparia": "Lapai sudėtiniai (11–15 lapelių). Vaisiai – oranžinės uogos, sukabintos kekėmis. Žievė lygi, pilka.",
    "Taxus baccata": "Tamsiai žali, plokšti, 2–3 cm spygliukai su dviem šviesiomis juostomis apačioje. Sėklos – su raudonu minkštu gaubtu.",
    "Tilia cordata": "Lapai širdiški, smulkiai dantyti, su ryškiomis gyslomis. Žiedai gelsvi, kvapnūs, su lapeliu-priedu.",
    "Ulmus glabra": "Dideli, šiurkštūs lapai su nelygiu pamatu. Vaisiai – plokšti, sparnuoti riešutėliai.",
    "Ulmus laevis": "Panaši į guobą, bet lapai lygesni, mažiau šiurkštūs, pamatas simetriškesnis.",
    "Ulmus minor": "Smulkesni lapai nei guobos, dažnai su kamštinėmis šakelėmis. Vaisiai – sparnuoti, su blakstienėlėmis.",
}

# ---------- model loading ----------
@st.cache_resource(show_spinner="Kraunami modeliai... / Loading models...")
def load_models():
    species_clf = joblib.load(APP_DIR / "species_clf.joblib")
    organ_clf = joblib.load(APP_DIR / "organ_clf.joblib")
    with open(APP_DIR / "meta.json", encoding="utf-8") as f:
        meta = json.load(f)
    device = "cuda" if torch.cuda.is_available() else "cpu"
    clip_model, _, preprocess = open_clip.create_model_and_transforms(MODEL_NAME)
    clip_model = clip_model.to(device).eval()
    return species_clf, organ_clf, meta, clip_model, preprocess, device


def embed_image(clip_model, preprocess, device, image_source):
    img = Image.open(image_source).convert("RGB")
    x = preprocess(img).unsqueeze(0).to(device)
    with torch.no_grad():
        f = clip_model.encode_image(x)
    return torch.nn.functional.normalize(f.float(), dim=-1).cpu().numpy()


# ---------- sidebar ----------
with st.sidebar:
    lang = st.selectbox(
        "🌐",
        options=list(LANG_NAMES.keys()),
        format_func=lambda k: LANG_NAMES[k],
        index=0,
        key="lang_selector",
    )

t = TEXTS[lang]

species_clf, organ_clf, meta, clip_model, preprocess, device = load_models()
classes = meta["classes"]
organs = meta["organs"]
latin_to_lt = meta["latin_to_lithuanian"]

with st.sidebar:
    st.divider()
    st.subheader(t["species_header"])
    st.caption(t["species_hint"])
    with st.container(height=380):
        for latin in sorted(latin_to_lt, key=lambda k: latin_to_lt[k]):
            if st.button(latin_to_lt[latin], key=f"sp_btn_{latin}", use_container_width=True):
                st.session_state["selected_species"] = latin

    sel = st.session_state.get("selected_species")
    st.divider()
    if sel:
        st.markdown(f"**{latin_to_lt.get(sel, sel)}**")
        st.caption(f"*{sel}*")
        st.write(SPECIES_DESCRIPTIONS.get(sel, ""))
    else:
        st.caption(t["pick_species"])

# ---------- header ----------
col_logo, col_title = st.columns([1, 9])
with col_logo:
    try:
        st.image(Image.open(APP_DIR / "logo.png"), width=90)
    except Exception:
        st.markdown(
            "<div style='font-size:64px;line-height:1;'>🌰</div>",
            unsafe_allow_html=True,
        )
with col_title:
    st.markdown(
        "<h2 style='margin-bottom:0.2rem;'>"
        "Paplitusių Lietuvos sumedėjusių augalų identifikavimo priemonė"
        "</h2>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<div class='small-grey'>"
        "Mokymosi priemonė dendrologijos studentams"
        "</div>",
        unsafe_allow_html=True,
    )

st.write("")

# ---------- how it works + privacy ----------
btn_col1, btn_col2, _ = st.columns([2, 2, 6])
with btn_col1:
    with st.popover(t["how"]):
        st.markdown(t["how_text"])
with btn_col2:
    with st.popover(t["privacy"]):
        st.markdown(t["privacy_text"])

st.divider()

# ---------- upload / camera ----------
tab_upload, tab_camera = st.tabs([t["upload"], t["camera"]])
with tab_upload:
    uploaded = st.file_uploader(
        t["upload"],
        type=["jpg", "jpeg", "png", "webp", "bmp"],
        label_visibility="collapsed",
        key="uploader",
    )
with tab_camera:
    camera_shot = st.camera_input(t["camera"], label_visibility="collapsed", key="camera")

image_source = uploaded if uploaded is not None else camera_shot

if image_source is None:
    st.info(t["no_image"])
else:
    col_img, col_pred = st.columns([1, 1])

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

            org_proba = organ_clf.predict_proba(feat)[0]
            org_classes = organ_clf.classes_
            org_full = np.zeros(len(organs))
            for idx, p in zip(org_classes, org_proba):
                org_full[idx] = p
            org_idx = int(org_full.argmax())

        top1 = order[0]
        st.subheader(t["prediction"])
        st.markdown(
            f"### {latin_to_lt.get(classes[top1], classes[top1])}\n"
            f"*{classes[top1]}* — {full[top1]:.1%} {t['confidence']}"
        )

        st.markdown(f"**{t['top3']}**")
        for i in order[:3]:
            latin = classes[i]
            lt = latin_to_lt.get(latin, latin)
            st.progress(
                float(full[i]),
                text=f"{lt} ({latin}) — {full[i]:.1%}",
            )

        st.markdown(f"**{t['organ']}**")
        st.progress(
            float(org_full[org_idx]),
            text=f"{organs[org_idx]} — {org_full[org_idx]:.1%}",
        )

        st.markdown(
            f"<div class='small-grey' style='margin-top:1rem;'>{t['disclaimer']}</div>",
            unsafe_allow_html=True,
        )

# ---------- footer ----------
st.markdown(
    f"<div class='footer-grey'>{t['footer']}</div>",
    unsafe_allow_html=True,
)
