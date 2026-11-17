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

APP_DIR = Path(__file__).parent
MODEL_NAME = "hf-hub:imageomics/bioclip"
LOGO_PATH = APP_DIR / "logo.png"

st.set_page_config(
    page_title="Lietuvos medžių identifikatorius",
    layout="wide",
)

# ---------- logo (for cursor) ----------
logo_b64 = ""
if LOGO_PATH.exists():
    try:
        logo_b64 = base64.b64encode(LOGO_PATH.read_bytes()).decode()
    except Exception:
        logo_b64 = ""

cursor_css = ""
if logo_b64:
    cursor_css = f"""
    html, body, .stApp, .stMarkdown, h1, h2, h3, h4, h5, h6, p, label,
    [data-testid="stSidebar"] {{
        cursor: url('data:image/png;base64,{logo_b64}') 16 16, auto !important;
    }}
    """

# ---------- styling (no brown, fresh green palette) ----------
st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    html, body, .stApp, .stMarkdown, .stText, .stCaption,
    .stSelectbox, .stTabs, .stInfo, .stWarning,
    h1, h2, h3, h4, h5, h6, p, label, button {{
        font-family: 'Inter', sans-serif !important;
    }}

    {cursor_css}

    .stApp {{ background-color: #F4F6F1 !important; color: #2B2B2B; }}
    .block-container {{ padding-top: 1.5rem; padding-bottom: 1rem; }}
    [data-testid="stSidebar"] {{ background-color: #E8EDE3 !important; }}

    h1, h2, h3, h4, h5 {{
        color: #1F3B2C !important;
        font-weight: 700;
        letter-spacing: -0.015em;
    }}
    h1 {{ font-size: 3.2rem !important; line-height: 1.1 !important; }}

    p, .stMarkdown, label {{ color: #2E2E2E; }}

    /* Buttons: very round, fresh green */
    .stButton > button,
    .stPopover > button,
    [data-testid="stPopover"] > button {{
        border-radius: 26px !important;
        background-color: #3E8E5A !important;
        color: #FFFFFF !important;
        border: 1px solid #347A4C !important;
        font-weight: 600 !important;
        padding: 0.6rem 1.25rem !important;
        transition: all 0.15s ease;
    }}
    .stButton > button:hover,
    .stPopover > button:hover,
    [data-testid="stPopover"] > button:hover {{
        background-color: #2F7548 !important;
        border-color: #2A6B40 !important;
        color: #FFFFFF !important;
        transform: translateY(-1px);
    }}

    /* Species list expanders: rounder, bold labels */
    [data-testid="stExpander"] details summary {{
        border-radius: 20px !important;
        background-color: #DEE7D8 !important;
        color: #1F3B2C !important;
        font-weight: 700 !important;
        border: 1px solid #C8D5BF !important;
        padding: 0.7rem 1rem !important;
    }}
    [data-testid="stExpander"] details[open] summary {{
        background-color: #D2DECB !important;
        border-color: #3E8E5A !important;
    }}

    /* Dropdowns: rounder */
    .stSelectbox > div > div {{
        border-radius: 22px !important;
        background-color: #FFFFFF !important;
        border: 1px solid #C8D5BF !important;
        padding: 0.25rem 0.75rem !important;
    }}

    /* Bigger upload area */
    [data-testid="stFileUploaderDropzone"],
    [data-testid="stFileUploader"] section {{
        min-height: 240px !important;
        border-radius: 22px !important;
        background-color: #FFFFFF !important;
        border: 2px dashed #3E8E5A !important;
        padding: 2.2rem !important;
    }}
    [data-testid="stFileUploaderDropzone"] svg,
    [data-testid="stFileUploader"] section svg {{
        width: 4rem !important;
        height: 4rem !important;
        color: #3E8E5A !important;
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
    .footer-grey {{
        color: #6B6B6B; font-size: 0.75rem; text-align: center;
        padding: 2.5rem 0 1rem 0;
    }}

    .feature-box {{
        background-color: #FFFFFF;
        border-left: 5px solid #3E8E5A;
        border-radius: 14px;
        padding: 1.1rem 1.3rem;
        margin: 0.9rem 0 1.2rem 0;
        color: #2E2E2E;
        font-size: 0.95rem;
        line-height: 1.6;
    }}
    .feature-box .feature-label {{
        font-weight: 700;
        color: #1F3B2C;
        margin-bottom: 0.45rem;
        font-size: 0.98rem;
    }}

    .alt-species {{
        background-color: #EDF2E9;
        border-radius: 14px;
        padding: 0.9rem 1.15rem;
        margin-bottom: 0.65rem;
        border: 1px solid #D2DECB;
    }}
    .alt-species .alt-name {{
        font-weight: 700;
        color: #1F3B2C;
        font-size: 1rem;
    }}
    .alt-species .alt-conf {{
        color: #3E8E5A;
        font-weight: 600;
        margin-left: 0.4rem;
    }}
    .alt-species .alt-reason {{
        color: #555;
        font-size: 0.88rem;
        margin-top: 0.3rem;
        line-height: 1.45;
    }}

    .top-pred-name {{
        font-size: 2.1rem;
        font-weight: 800;
        color: #1F3B2C;
        margin-bottom: 0.15rem;
        line-height: 1.15;
    }}
    .top-pred-conf {{
        font-size: 1.15rem;
        color: #3E8E5A;
        font-weight: 700;
        margin-bottom: 0.2rem;
    }}
    .top-pred-latin {{
        color: #666;
        font-style: italic;
        font-size: 0.95rem;
        margin-bottom: 0.5rem;
    }}

    [data-testid="stTabs"] button[role="tab"] {{
        border-radius: 14px 14px 0 0;
        color: #1F3B2C;
    }}
    [data-testid="stTabs"] button[role="tab"][aria-selected="true"] {{
        background-color: #DEE7D8;
        border-bottom-color: #3E8E5A;
    }}

    #MainMenu {{ visibility: hidden; }}
    footer {{ visibility: hidden; }}
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- language names ----------
LANG_NAMES = {
    "lt": "Lietuvių",
    "en": "English",
    "de": "Deutsch",
    "fr": "Français",
    "es": "Español",
    "uk": "Українська",
}

# ---------- translations ----------
TEXTS = {
    "lt": {
        "title": "Paplitusių Lietuvos sumedėjusių augalų identifikavimo priemonė",
        "subtitle": "Mokymosi priemonė dendrologijos studentams",
        "lang_label": "Kalba",
        "upload": "Įkelkite nuotrauką",
        "camera": "Fotografuoti",
        "how": "Kaip ši programėlė veikia?",
        "how_text": (
            "Programa naudoja dirbtinio intelekto modelį **BioCLIP**, kuris nuotrauką "
            "paverčia skaitmeniniu „pirštų atspaudu“ (įterpiniu). Tada logistinės "
            "regresijos klasifikatorius, apmokytas su ~23 000 iNaturalist nuotraukų, "
            "palygina jūsų nuotrauką su 28 Lietuvos medžių rūšimis ir išrenka "
            "tikimiausią.\n\n"
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
        "species_header": "Įrankio atpažįstamų rūšių sąrašas",
        "species_hint": "Spustelėkite rūšį, kad pamatytumėte aprašymą.",
        "top3": "Kitos galimos rūšys",
        "confidence": "pasitikėjimas",
        "analyzing": "Tikrinu...",
        "no_image": "Įkelkite nuotrauką – ir kartu išsiaiškinsime, kas čia auga.",
        "feature_label": "Pagrindiniai atpažinimo požymiai",
        "disclaimer": (
            "Tai dirbtinio intelekto įrankis – jis gali klysti. "
            "Rekomenduojama rūšį patikrinti su dėstytoju."
        ),
        "footer": "Tai studentų projektas, sukurtas dirbtinio intelekto kurso metu.",
    },
    "en": {
        "title": "Identification Tool for Common Lithuanian Woody Plants",
        "subtitle": "A learning tool for dendrology students",
        "lang_label": "Language",
        "upload": "Upload a photo",
        "camera": "Take a photo",
        "how": "How does this app work?",
        "how_text": (
            "The app uses the **BioCLIP** AI model to turn your photo into a numeric "
            "“fingerprint” (embedding). A logistic-regression classifier, trained on "
            "~23,000 iNaturalist photos, then compares your photo against 28 Lithuanian "
            "tree species and picks the most likely one.\n\n"
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
        "species_header": "List of species the tool recognises",
        "species_hint": "Click a species to see its description.",
        "top3": "Other possible species",
        "confidence": "confidence",
        "analyzing": "Checking...",
        "no_image": "Upload a photo – let's figure out together what grows here.",
        "feature_label": "Key identification features",
        "disclaimer": (
            "This is an AI tool and it can be wrong. "
            "Please check the species with your professor."
        ),
        "footer": "This is a student project made for an AI class.",
    },
    "de": {
        "title": "Bestimmungshilfe für verbreitete litauische Gehölze",
        "subtitle": "Ein Lernwerkzeug für Dendrologie-Studierende",
        "lang_label": "Sprache",
        "upload": "Foto hochladen",
        "camera": "Foto aufnehmen",
        "how": "Wie funktioniert diese App?",
        "how_text": (
            "Die App nutzt das KI-Modell **BioCLIP**, um dein Foto in einen numerischen "
            "„Fingerabdruck“ (Embedding) umzuwandeln. Ein logistischer Regressions-"
            "Klassifikator, trainiert mit ~23.000 iNaturalist-Fotos, vergleicht dein Foto "
            "mit 28 litauischen Baumarten und wählt die wahrscheinlichste.\n\n"
            "**So geht's:** Foto hochladen (oder mit dem Handy knipsen), ein paar "
            "Sekunden warten. Links kannst du alle 28 Arten durchstöbern."
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
        "species_header": "Liste der erkannten Arten",
        "species_hint": "Klicke auf eine Art, um die Beschreibung zu sehen.",
        "top3": "Andere mögliche Arten",
        "confidence": "Konfidenz",
        "analyzing": "Prüfe...",
        "no_image": "Lade ein Foto hoch – finden wir gemeinsam heraus, was hier wächst.",
        "feature_label": "Wichtige Bestimmungsmerkmale",
        "disclaimer": (
            "Dies ist ein KI-Werkzeug und kann Fehler machen. "
            "Bitte überprüfe die Art mit deinem Professor."
        ),
        "footer": "Dies ist ein Studierendenprojekt für einen KI-Kurs.",
    },
    "fr": {
        "title": "Outil d'identification des plantes ligneuses lituaniennes communes",
        "subtitle": "Un outil pédagogique pour les étudiants en dendrologie",
        "lang_label": "Langue",
        "upload": "Téléverser une photo",
        "camera": "Prendre une photo",
        "how": "Comment fonctionne cette application ?",
        "how_text": (
            "L'application utilise le modèle d'IA **BioCLIP** pour transformer votre "
            "photo en une « empreinte » numérique (embedding). Un classificateur de "
            "régression logistique, entraîné sur ~23 000 photos iNaturalist, compare "
            "ensuite votre photo à 28 espèces d'arbres lituaniens et choisit la plus "
            "probable.\n\n"
            "**Mode d'emploi :** téléversez une photo (ou prenez-en une avec votre "
            "téléphone) et patientez quelques secondes."
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
        "species_header": "Liste des espèces reconnues par l'outil",
        "species_hint": "Cliquez sur une espèce pour voir sa description.",
        "top3": "Autres espèces possibles",
        "confidence": "confiance",
        "analyzing": "Vérification...",
        "no_image": "Téléversez une photo – et découvrons ensemble ce qui pousse ici.",
        "feature_label": "Principaux caractères d'identification",
        "disclaimer": (
            "Cet outil d'IA peut se tromper. "
            "Veuillez vérifier l'espèce avec votre professeur."
        ),
        "footer": "Projet étudiant réalisé pour un cours d'IA.",
    },
    "es": {
        "title": "Herramienta de identificación de plantas leñosas lituanas comunes",
        "subtitle": "Una herramienta de aprendizaje para estudiantes de dendrología",
        "lang_label": "Idioma",
        "upload": "Subir una foto",
        "camera": "Tomar una foto",
        "how": "¿Cómo funciona esta aplicación?",
        "how_text": (
            "La aplicación usa el modelo de IA **BioCLIP** para convertir tu foto en una "
            "«huella» numérica (embedding). Un clasificador de regresión logística, "
            "entrenado con ~23 000 fotos de iNaturalist, compara tu foto con 28 especies "
            "de árboles lituanos y elige la más probable.\n\n"
            "**Cómo usarla:** sube una foto (o hazla con el móvil) y espera unos "
            "segundos."
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
        "species_header": "Lista de especies que reconoce la herramienta",
        "species_hint": "Haz clic en una especie para ver su descripción.",
        "top3": "Otras especies posibles",
        "confidence": "confianza",
        "analyzing": "Comprobando...",
        "no_image": "Sube una foto y descubramos juntos qué crece aquí.",
        "feature_label": "Principales características de identificación",
        "disclaimer": (
            "Esta herramienta de IA puede equivocarse. "
            "Verifica la especie con tu profesor."
        ),
        "footer": "Proyecto estudiantil realizado para un curso de IA.",
    },
    "uk": {
        "title": "Інструмент для визначення поширених литовських деревних рослин",
        "subtitle": "Навчальний інструмент для студентів-дендрологів",
        "lang_label": "Мова",
        "upload": "Завантажити фото",
        "camera": "Зробити фото",
        "how": "Як працює цей застосунок?",
        "how_text": (
            "Застосунок використовує модель ШІ **BioCLIP**, яка перетворює вашу "
            "фотографію на числовий «відбиток» (ембединг). Потім класифікатор "
            "логістичної регресії, навчений на ~23 000 фотографій iNaturalist, "
            "порівнює ваше фото з 28 видами литовських дерев і вибирає найімовірніший."
            "\n\n**Як користуватися:** завантажте фото (або сфотографуйте телефоном) і "
            "зачекайте кілька секунд."
        ),
        "privacy": "Політика конфіденційності (GDPR)",
        "privacy_text": (
            "Цей застосунок **не зберігає** ваші фотографії. Зображення обробляються "
            "лише в пам'яті сервера, поки формується відповідь, і одразу видаляються. "
            "Ми не збираємо персональні дані й не використовуємо маркетингові cookie."
            "\n\nЗ питань обробки даних відповідно до **GDPR** (Регламент 2016/679) "
            "звертайтеся до автора проєкту (студента)."
        ),
        "species_header": "Список видів, які розпізнає інструмент",
        "species_hint": "Натисніть на вид, щоб побачити опис.",
        "top3": "Інші можливі види",
        "confidence": "впевненість",
        "analyzing": "Перевіряю...",
        "no_image": "Завантажте фото – і разом з'ясуємо, що тут росте.",
        "feature_label": "Основні ідентифікаційні ознаки",
        "disclaimer": (
            "Це інструмент ШІ, і він може помилятися. "
            "Будь ласка, перевірте вид разом із викладачем."
        ),
        "footer": "Студентський проєкт, створений для курсу зі штучного інтелекту.",
    },
}

# ---------- species data (same as before — full translations) ----------
SPECIES_DATA = {
    "Acer platanoides": {
        "names": {"lt": "Paprastasis klevas", "en": "Norway maple", "de": "Spitzahorn",
                   "fr": "Érable plane", "es": "Arce real", "uk": "Клен гостролистий"},
        "desc": {
            "lt": "Lapai plačiai skiltuoti – paprastai su penkiomis skiltimis, tarsi atversta ranka – rudenį įsiplieskia auksine geltona ir oranžine spalva. Jauna žievė lygi ir žalia, vėliau tamsėja ir išilgai vagėja. Vaisiai – sparnuoti sparnavaisiai, kabantys poromis tarsi maži propeleriukai. Dažnas parkuose, skveruose ir derlingesniuose miškuose.",
            "en": "Broadly lobed leaves – usually with five lobes, like an open hand – flare gold and orange in autumn. Young bark is smooth and green, later darkening and furrowing lengthwise. Fruits are paired winged samaras hanging like little propellers. Common in parks, squares, and fertile woodland.",
            "de": "Breit gelappte Blätter – meist mit fünf Lappen, wie eine offene Hand – leuchten im Herbst gold und orange. Junge Rinde ist glatt und grün, später dunkelt sie nach und wird längs gefurcht. Früchte sind paarweise hängende geflügelte Spaltfrüchte wie kleine Propeller.",
            "fr": "Feuilles largement lobées – en général à cinq lobes, comme une main ouverte – qui flamboient d'or et d'orange en automne. L'écorce jeune est lisse et verte, puis fonce et se fissure. Les fruits sont des samares ailées suspendues par paires comme de petites hélices.",
            "es": "Hojas ampliamente lobuladas – normalmente con cinco lóbulos, como una mano abierta – que se encienden de dorado y naranja en otoño. La corteza joven es lisa y verde, luego oscurece y se agrieta. Los frutos son sámaras aladas colgando en parejas como pequeñas hélices.",
            "uk": "Широко лопатеві листки – зазвичай із п'ятьма лопатями, мов розкрита долоня – восени спалахують золотом та оранжем. Молода кора гладенька й зелена, згодом темніє та вкривається поздовжніми тріщинами. Плоди – крилаті двосім'янки, що звисають парами, наче маленькі пропелери.",
        },
    },
    "Alnus glutinosa": {
        "names": {"lt": "Juodalksnis", "en": "Black alder", "de": "Schwarz-Erle",
                   "fr": "Aulne glutineux", "es": "Aliso negro", "uk": "Вільха чорна"},
        "desc": {
            "lt": "Lapai atvirkščiai kiaušiniški, su būdingu įkirptu viršūniu – tarsi kas būtų nukandęs galiuką. Jauni jie lipnūs, vėliau tampa blizgūs, tamsiai žali. Žievė tamsi, giliai sueižėjusi, sena – beveik juoda. Mėgsta šlapias, pelkėtas vietas prie vandens.",
            "en": "Leaves are obovate with a characteristic notched tip – as if someone had nibbled the end. Sticky when young, later becoming glossy dark green. Bark is dark, deeply fissured, almost black when old. Loves wet, swampy sites beside water.",
            "de": "Blätter sind verkehrt-eiförmig mit einer typischen eingekerbten Spitze – als hätte jemand hineingebissen. Jung klebrig, später glänzend dunkelgrün. Die Rinde ist dunkel und tief gefurcht, im Alter fast schwarz.",
            "fr": "Feuilles obovales à pointe caractéristique échancrée – comme si quelqu'un avait mordu le bout. Collantes jeunes, puis luisantes et vert foncé. L'écorce est sombre, profondément fissurée, presque noire en vieillissant.",
            "es": "Hojas obovadas con una característica punta escotada – como si alguien le hubiera dado un mordisco. Pegajosas de jóvenes, luego brillantes y verde oscuro. La corteza es oscura, profundamente agrietada, casi negra en la vejez.",
            "uk": "Листки обернено-яйцеподібні, з характерною виїмкою на верхівці – наче хтось відкусив кінчик. Молоді – клейкі, згодом стають блискучими, темно-зеленими. Кора темна, глибоко потріскана, у старості майже чорна.",
        },
    },
    "Alnus incana": {
        "names": {"lt": "Baltalksnis", "en": "Grey alder", "de": "Grau-Erle",
                   "fr": "Aulne blanc", "es": "Aliso gris", "uk": "Вільха сіра"},
        "desc": {
            "lt": "Lapai smailūs, plačiai kiaušiniški arba elipsiški, dantyti – jų apatinė pusė pilkai plaukuota, todėl nuo tolo atrodo tarsi sidabrinė. Žievė lygi, šviesiai pilka, todėl lengvai atskiriama nuo tamsios juodalksnio žievės. Auga pakelėse, upių slėniuose, sausringesnėse vietose nei juodalksnis.",
            "en": "Leaves are pointed, broadly ovate or elliptical, toothed – their underside is grey-hairy, giving the tree a silvery look from afar. Bark is smooth and light grey, easy to tell apart from the dark bark of black alder. Grows along roadsides and in river valleys.",
            "de": "Blätter zugespitzt, breit eiförmig oder elliptisch, gezähnt – ihre Unterseite ist grau behaart, wodurch der Baum aus der Ferne silbrig wirkt. Rinde glatt und hellgrau, gut von der dunklen Rinde der Schwarz-Erle zu unterscheiden.",
            "fr": "Feuilles pointues, largement ovales ou elliptiques, dentées – leur dessous est gris-poilu, donnant à l'arbre un aspect argenté. L'écorce est lisse et gris clair, facile à distinguer de celle, sombre, de l'aulne glutineux.",
            "es": "Hojas puntiagudas, anchamente ovadas o elípticas, dentadas – su envés es gris-peloso, lo que da al árbol un aspecto plateado. La corteza es lisa y gris claro, fácil de distinguir de la corteza oscura del aliso negro.",
            "uk": "Листки загострені, широко-яйцеподібні або еліптичні, зубчасті – їхній низ сіро-опушений, тому здалеку дерево виглядає сріблястим. Кора гладенька, світло-сіра.",
        },
    },
    "Betula pendula": {
        "names": {"lt": "Karpotasis beržas", "en": "Silver birch", "de": "Hänge-Birke",
                   "fr": "Bouleau verruqueux", "es": "Abedul común", "uk": "Береза повисла"},
        "desc": {
            "lt": "Balta žievė su horizontaliomis juodomis juostelėmis – tarsi kas būtų braukęs anglimi. Jaunos šakelės karpotos, todėl ir vadinamas karpotuoju. Lapai rombiški, smailūs, dvigubai dantyti, rudenį paauksuoja. Jauni medžiai turi gražiai nusvirusias šakeles.",
            "en": "White bark with horizontal black bands – as if drawn with charcoal. Young twigs are warty, which gives it its name. Leaves are rhombic, pointed, doubly toothed, turning gold in autumn. Young trees have gracefully weeping branches.",
            "de": "Weiße Rinde mit waagerechten schwarzen Bändern – als wären sie mit Kohle gezeichnet. Junge Zweige sind warzig. Blätter rhombisch, zugespitzt, doppelt gezähnt, im Herbst golden. Junge Bäume haben anmutig überhängende Zweige.",
            "fr": "Écorce blanche aux bandes noires horizontales – comme dessinées au fusain. Les jeunes rameaux sont verruqueux. Feuilles rhombiques, pointues, doublement dentées, dorées en automne. Les jeunes arbres ont des branches gracieusement pleureuses.",
            "es": "Corteza blanca con bandas negras horizontales – como dibujadas con carbón. Las ramillas jóvenes son verrugosas. Hojas rómbicas, puntiagudas, doblemente dentadas, que se vuelven doradas en otoño.",
            "uk": "Біла кора з горизонтальними чорними смугами – наче намальованими вугіллям. Молоді пагони горбкуваті. Листки ромбічні, загострені, двічі зубчасті, восени золотіють.",
        },
    },
    "Betula pubescens": {
        "names": {"lt": "Plaukuotasis beržas", "en": "Downy birch", "de": "Moor-Birke",
                   "fr": "Bouleau pubescent", "es": "Abedul pubescente", "uk": "Береза пухнаста"},
        "desc": {
            "lt": "Labai panašus į karpotąjį beržą – bet jaunos šakelės ir lapai plaukuoti, be karpių, todėl jį atskirti padeda lietimas. Lapai platesni, šiek tiek širdiški, trumpesniais koteliais. Žievė balta, bet žemyn link kamieno dažnai tamsėja. Mėgsta drėgnesnes vietas.",
            "en": "Very similar to silver birch – but its young twigs and leaves are hairy, without warts, so a gentle touch helps tell them apart. Leaves are broader, somewhat heart-shaped. Bark is white but often darkens lower down. Prefers wetter sites.",
            "de": "Sehr ähnlich der Hänge-Birke – aber junge Zweige und Blätter sind behaart, ohne Warzen. Blätter breiter, etwas herzförmig, mit kürzeren Stielen. Rinde weiß, wird aber weiter unten am Stamm oft dunkel.",
            "fr": "Très semblable au bouleau verruqueux – mais ses jeunes rameaux et ses feuilles sont poilus, sans verrues. Feuilles plus larges, un peu cordiformes. L'écorce est blanche mais s'assombrit souvent vers le bas du tronc.",
            "es": "Muy similar al abedul común – pero sus ramillas y hojas jóvenes son peludas, sin verrugas. Hojas más anchas, algo acorazonadas. La corteza es blanca pero a menudo oscurece hacia la base del tronco.",
            "uk": "Дуже схожа на березу повислу – але молоді пагони й листки пухнасті, без горбиків. Листки ширші, трохи серцеподібні. Кора біла, але ближче до основи стовбура часто темніє.",
        },
    },
    "Carpinus betulus": {
        "names": {"lt": "Paprastasis skroblas", "en": "European hornbeam", "de": "Hainbuche",
                   "fr": "Charme", "es": "Carpe blanco", "uk": "Граб звичайний"},
        "desc": {
            "lt": "Lapai ovalūs, dantyti, su labai ryškiomis gyslomis – tarsi suraukti. Žievė lygi, pilka, su būdingu „raumenų“ raštu – ja net sunku patikėti, kad tai medis. Vaisiai – smulkūs riešutėliai, kiekvienas su trijų skilčių lapeliu-kapučiu. Auga derlingose, drėgnose dirvose.",
            "en": "Leaves are oval, toothed, with very prominent veins – as if wrinkled. Bark is smooth and grey with a characteristic 'muscular' pattern – hard to believe it belongs to a tree. Fruits are small nutlets, each with a three-lobed bract.",
            "de": "Blätter sind oval, gezähnt, mit sehr ausgeprägten Adern – wie gerunzelt. Die Rinde ist glatt und grau mit einem typischen „muskulösen“ Muster. Die Früchte sind kleine Nüsschen mit dreilappigem Hochblatt.",
            "fr": "Feuilles ovales, dentées, aux nervures très marquées – comme ridées. L'écorce est lisse et grise, avec un motif «musclé» caractéristique. Les fruits sont de petites noisettes à bractée trilobée.",
            "es": "Hojas ovaladas, dentadas, con nervios muy marcados – como arrugadas. La corteza es lisa y gris con un patrón «musculoso» característico. Los frutos son pequeñas nuececillas con bráctea trilobulada.",
            "uk": "Листки овальні, зубчасті, з дуже виразними жилками – наче зморшкуваті. Кора гладенька, сіра, з характерним «мускулястим» візерунком. Плоди – дрібні горішки з трилопатевою обгорткою.",
        },
    },
    "Fagus sylvatica": {
        "names": {"lt": "Paprastasis bukas", "en": "European beech", "de": "Rotbuche",
                   "fr": "Hêtre", "es": "Haya", "uk": "Бук лісовий"},
        "desc": {
            "lt": "Lapai blizgūs, elipsiški, lygiais kraštais – rudenį nusidažo varine ruda spalva, kuri ilgai išlieka ant medžio. Žievė lygi, plona, šviesiai pilka, net sena lieka lygi – ant jos mėgsta raižyti įsimylėjėliai. Riešutai – trikampiai bukučiai, paslėpti dygliuotame gaubte. Mėgsta derlingas, kalkingas dirvas.",
            "en": "Leaves are glossy, elliptical, with smooth margins – in autumn they turn a copper brown that lingers on the tree. Bark is smooth, thin and pale grey, remaining smooth even on old trees. Nuts are triangular beechnuts hidden inside a spiny husk.",
            "de": "Blätter glänzend, elliptisch, ganzrandig – im Herbst kupferbraun. Die Rinde ist glatt, dünn und hellgrau, selbst alte Bäume bleiben glatt. Früchte sind dreikantige Bucheckern in einer stacheligen Hülle.",
            "fr": "Feuilles luisantes, elliptiques, à bord lisse – en automne brun cuivré. L'écorce est lisse, fine et gris pâle, restant lisse même sur les vieux arbres. Fruits : faînes triangulaires dans une cupule épineuse.",
            "es": "Hojas brillantes, elípticas, de margen liso – en otoño marrón cobrizo. La corteza es lisa, fina y gris claro. Los frutos son hayucos triangulares en una cúpula espinosa.",
            "uk": "Листки блискучі, еліптичні, з рівним краєм – восени мідно-бурі. Кора гладенька, тонка, світло-сіра. Плоди – трикутні горішки в колючій обгортці.",
        },
    },
    "Fraxinus excelsior": {
        "names": {"lt": "Paprastasis uosis", "en": "European ash", "de": "Gewöhnliche Esche",
                   "fr": "Frêne commun", "es": "Fresno común", "uk": "Ясен звичайний"},
        "desc": {
            "lt": "Lapai sudėtiniai, paprastai su 5–9 lapeliais, išsidėstę priešais – tarsi žalių plunksnų poros. Žiemą uosį lengviausia atpažinti iš juodų, aksominių pumpurų – jie tarsi maži juodi kačiukai. Vaisiai – sparnuoti riešutėliai, sukabinti kekėmis. Auga derlingose, drėgnose dirvose.",
            "en": "Leaves are pinnately compound, usually with 5–9 leaflets in opposite pairs – like pairs of green feathers. In winter, ash is easiest to recognise by its black, velvety buds. Fruits are winged samaras clustered in hanging bunches.",
            "de": "Blätter gefiedert, meist mit 5–9 gegenständigen Fiederblättchen – wie Paare grüner Federn. Im Winter erkennt man die Esche an ihren schwarzen, samtigen Knospen. Früchte sind geflügelte Spaltfrüchte in hängenden Büscheln.",
            "fr": "Feuilles composées pennées, généralement à 5–9 folioles opposées – comme des paires de plumes vertes. En hiver, on reconnaît le frêne à ses bourgeons noirs et veloutés. Fruits : samares ailées en grappes pendantes.",
            "es": "Hojas compuestas pinnadas, normalmente con 5–9 foliolos opuestos – como pares de plumas verdes. En invierno se reconoce por sus yemas negras y aterciopeladas. Frutos: sámaras aladas en racimos colgantes.",
            "uk": "Листки складні, пірчасті, зазвичай із 5–9 листочками – наче пари зелених пір'їн. Узимку ясен впізнають за чорними оксамитовими бруньками. Плоди – крилаті двосім'янки в пониклих пучках.",
        },
    },
    "Juniperus communis": {
        "names": {"lt": "Paprastasis kadagys", "en": "Common juniper", "de": "Gewöhnlicher Wacholder",
                   "fr": "Genévrier commun", "es": "Enebro común", "uk": "Ялівець звичайний"},
        "desc": {
            "lt": "Krūmas arba mažas medis, dažnai kūgiškos formos – iš tolo gali atrodyti kaip maža eglutė. Spygliai dygliuoti, 1–2 cm ilgio, išsidėstę po tris ratuose. Uogų kekės melsvai juodos, apvalios, sunoksta net dvejus metus. Auga sausuose, smėlėtuose arba uolėtuose plotuose.",
            "en": "A shrub or small tree, often conical – from afar it may look like a little fir. Needles are prickly, 1–2 cm long, in whorls of three. Berry-like cones are bluish-black and ripen over two years. Grows in dry, sandy or rocky sites.",
            "de": "Ein Strauch oder kleiner Baum, oft kegelförmig. Nadeln stechend, 1–2 cm lang, in Dreierquirlen. Beerenzapfen bläulich-schwarz, reifen über zwei Jahre. Wächst an trockenen, sandigen oder felsigen Standorten.",
            "fr": "Un arbuste ou petit arbre, souvent conique. Aiguilles piquantes, longues de 1–2 cm, en verticilles de trois. Cônes-berries bleu-noir, mûrissant sur deux ans. Pousse dans des sites secs, sablonneux ou rocheux.",
            "es": "Un arbusto o pequeño árbol, a menudo cónico. Acículas punzantes, de 1–2 cm, en verticilos de tres. Conos-baya azul negruzcos, maduran en dos años. Crece en lugares secos, arenosos o rocosos.",
            "uk": "Кущ або невелике дерево, часто конічної форми. Голки колючі, 1–2 см, розташовані по три в кільцях. Шишкоягоди синювато-чорні, достигають два роки. Росте на сухих піщаних або кам'янистих місцях.",
        },
    },
    "Larix decidua": {
        "names": {"lt": "Europinis maumedis", "en": "European larch", "de": "Europäische Lärche",
                   "fr": "Mélèze d'Europe", "es": "Alerce europeo", "uk": "Модрина європейська"},
        "desc": {
            "lt": "Vienintelis Lietuvoje spyglius numetantis spygliuotis – rudenį spygliai nusidažo aukso geltonumo ir nukrinta. Spygliai minkšti, šviesiai žali, auga kekėmis ant trumpųjų ūglių – liesdamas nesudursi. Kankorėžiai smulkūs, kiaušiniški, 2–4 cm ilgio. Auga greitai, mėgsta šviesą ir derlingas dirvas.",
            "en": "The only deciduous conifer in Lithuania – its needles turn golden-yellow in autumn and drop. Needles are soft, light green, in tufts on short shoots – no prickles when you touch them. Cones are small, ovoid, 2–4 cm long. Grows fast, prefers light and fertile soils.",
            "de": "Der einzige sommergrüne Nadelbaum Litauens – Nadeln werden im Herbst goldgelb und fallen ab. Nadeln weich, hellgrün, in Büscheln an Kurztrieben. Zapfen klein, eiförmig, 2–4 cm. Wächst schnell, bevorzugt Licht.",
            "fr": "Le seul conifère caduc de Lituanie – ses aiguilles jaunissent en automne et tombent. Aiguilles douces, vert clair, en touffes. Cônes petits, ovoïdes, longs de 2–4 cm. Pousse vite, préfère la lumière.",
            "es": "La única conífera caducifolia de Lituania – sus acículas se vuelven amarillas y caen. Acículas suaves, verde claro, en manojos. Conos pequeños, ovoides, de 2–4 cm. Crece rápido, prefiere la luz.",
            "uk": "Єдина в Литві листопадна хвойна – голки восени жовтіють і опадають. Голки м'які, світло-зелені, пучками. Шишки дрібні, 2–4 см. Росте швидко, любить світло.",
        },
    },
    "Malus sylvestris": {
        "names": {"lt": "Miškinė obelis", "en": "European crab apple", "de": "Holzapfel",
                   "fr": "Pommier sauvage", "es": "Manzano silvestre", "uk": "Яблуня лісова"},
        "desc": {
            "lt": "Nedidelis medis, dažnai su dygliuotomis šakelėmis. Lapai ovalūs, dantyti, blizgūs. Žiedai balti arba rausvi, kvapnūs, žydi gegužę. Vaisiai – smulkūs, rūgštūs obuoliai, subręsta rugsėjį. Auga miškų pakraščiuose ir krūmynuose.",
            "en": "A small tree, often with thorny twigs. Leaves are oval, toothed, glossy. Flowers are white or pinkish, fragrant, blooming in May. Fruits are small, sour apples ripening in September. Grows in woodland edges and thickets.",
            "de": "Ein kleiner Baum, oft mit dornigen Zweigen. Blätter oval, gezähnt, glänzend. Blüten weiß oder rosastichig, duftend, im Mai. Früchte sind kleine, saure Äpfel im September. Wächst an Waldrändern.",
            "fr": "Un petit arbre, souvent à rameaux épineux. Feuilles ovales, dentées, luisantes. Fleurs blanches ou rosées, parfumées, en mai. Fruits : petites pommes acides mûrissant en septembre. Pousse en lisière de bois.",
            "es": "Un árbol pequeño, a menudo con ramillas espinosas. Hojas ovaladas, dentadas, brillantes. Flores blancas o rosadas, fragantes, en mayo. Frutos: manzanas pequeñas y ácidas en septiembre. Crece en bordes de bosque.",
            "uk": "Невелике дерево, часто з колючими пагонами. Листки овальні, зубчасті, блискучі. Квіти білі або рожевуваті, запашні, у травні. Плоди – дрібні кислі яблука у вересні. Росте на узліссях і в чагарниках.",
        },
    },
    "Picea abies": {
        "names": {"lt": "Paprastoji eglė", "en": "Norway spruce", "de": "Gemeine Fichte",
                   "fr": "Épicéa commun", "es": "Picea común", "uk": "Ялина європейська"},
        "desc": {
            "lt": "Siaurai piramidinis, simetriškas medis su nusvirusiomis šakomis – klasikinė Kalėdų eglutė. Spygliai tamsiai žali, 1–2,5 cm ilgio, išsidėstę spirališkai aplink šakelę. Kankorėžiai ilgi, cilindriški, kabantys žemyn. Auga derlingose, drėgnose dirvose, dažna mišriuose miškuose.",
            "en": "A narrowly pyramidal, symmetrical tree with drooping branches – the classic Christmas tree. Needles are dark green, 1–2.5 cm long, spirally arranged. Cones are long, cylindrical, and hang downwards. Grows on fertile, moist soils.",
            "de": "Ein schmal-pyramidaler, symmetrischer Baum mit überhängenden Zweigen – der klassische Weihnachtsbaum. Nadeln dunkelgrün, 1–2,5 cm lang, spiralig. Zapfen lang, zylindrisch, hängend.",
            "fr": "Un arbre étroitement pyramidal et symétrique aux branches retombantes – le sapin de Noël classique. Aiguilles vert foncé, 1–2,5 cm, en spirale. Cônes longs, cylindriques, pendants.",
            "es": "Un árbol estrechamente piramidal y simétrico con ramas colgantes – el clásico árbol de Navidad. Acículas verde oscuro, 1–2,5 cm, en espiral. Conos largos, cilíndricos, colgantes.",
            "uk": "Вузько-пірамідальне, симетричне дерево з пониклими гілками – класична різдвяна ялинка. Голки темно-зелені, 1–2,5 см, спірально. Шишки довгі, циліндричні, звисають.",
        },
    },
    "Pinus sylvestris": {
        "names": {"lt": "Paprastoji pušis", "en": "Scots pine", "de": "Waldkiefer",
                   "fr": "Pin sylvestre", "es": "Pino silvestre", "uk": "Сосна звичайна"},
        "desc": {
            "lt": "Spygliai 4–7 cm ilgio, išsidėstę po du ir šiek tiek susisukę – tarsi mažos žalios žirklės. Viršutinė kamieno žievė oranžiškai rausva, pleiskanojanti plokštelėmis – iš tolo atrodo lyg įdegusi. Kankorėžiai smulkūs, kūgiški. Auga sausuose, smėlėtuose plotuose.",
            "en": "Needles 4–7 cm long, in pairs and slightly twisted – like small green scissors. The upper trunk bark is orange-red, flaking in plates – it looks sun-tanned from afar. Cones are small and conical. Grows on dry, sandy sites.",
            "de": "Nadeln 4–7 cm lang, paarweise und leicht gedreht. Rinde des oberen Stamms orangerot, in Platten abblätternd. Zapfen klein und kegelförmig. Wächst an trockenen, sandigen Standorten.",
            "fr": "Aiguilles longues de 4–7 cm, groupées par deux et légèrement torsadées. Écorce du haut du tronc orange-rouge, s'écaillant en plaques. Cônes petits et coniques. Pousse dans des sites secs et sablonneux.",
            "es": "Acículas de 4–7 cm, agrupadas por pares y algo retorcidas. Corteza de la parte alta del tronco naranja rojizo, descamándose. Conos pequeños y cónicos. Crece en lugares secos y arenosos.",
            "uk": "Голки 4–7 см, зібрані по дві й трохи скручені. Кора верхньої частини стовбура оранжево-руда, відшаровується пластинками. Шишки дрібні, конічні. Росте на сухих піщаних місцях.",
        },
    },
    "Populus nigra": {
        "names": {"lt": "Juodoji tuopa", "en": "Black poplar", "de": "Schwarz-Pappel",
                   "fr": "Peuplier noir", "es": "Álamo negro", "uk": "Тополя чорна"},
        "desc": {
            "lt": "Storas, plačiai išsišakojęs kamienas su tamsia, giliai sueižėjusia žieve – atrodo tarsi raukšlėtas dramblio odos. Lapai trikampiški arba rombiški, smailūs, ilgais koteliais. Auga upių slėniuose, drėgnose, derlingose dirvose. Šiuo metu tai reta, saugoma rūšis.",
            "en": "A thick, widely branching trunk with dark, deeply fissured bark – like wrinkled elephant skin. Leaves are triangular or rhombic, pointed, with long petioles. Grows in river valleys on moist, fertile soils. Now a rare, protected species.",
            "de": "Ein dicker, breit verzweigter Stamm mit dunkler, tief gefurchter Rinde – wie runzlige Elefantenhaut. Blätter dreieckig oder rhombisch. Wächst in Flusstälern auf feuchten, fruchtbaren Böden. Selten und geschützt.",
            "fr": "Un tronc épais et largement ramifié à l'écorce sombre et profondément fissurée – comme une peau d'éléphant ridée. Feuilles triangulaires ou rhombiques. Pousse dans les vallées fluviales sur des sols humides. Rare et protégé.",
            "es": "Un tronco grueso y muy ramificado con corteza oscura y profundamente agrietada – como piel de elefante arrugada. Hojas triangulares o rómbicas. Crece en valles fluviales sobre suelos húmedos. Raro y protegido.",
            "uk": "Товстий, широко розгалужений стовбур із темною, глибоко потрісканою корою – наче зморшкувата слоняча шкіра. Листки трикутні або ромбічні. Росте в річкових долинах на вологих ґрунтах. Рідкісний, охоронюваний вид.",
        },
    },
    "Populus tremula": {
        "names": {"lt": "Drebulė", "en": "Eurasian aspen", "de": "Zitter-Pappel",
                   "fr": "Peuplier tremble", "es": "Álamo temblón", "uk": "Осика"},
        "desc": {
            "lt": "Lapai apvalūs, ilgais, plokščiais koteliais – todėl jie virpa net lengvame vėjyje. Žievė lygi, pilkai žalia, su rombiškomis „akimis“. Rudenį lapai tampa raudoni arba geltoni. Auga miškų pakraščiuose, dažnai drėgnose vietose.",
            "en": "Leaves are rounded with long, flattened petioles – so they tremble even in a light breeze. Bark is smooth, grey-green, with diamond-shaped 'eyes'. In autumn the leaves turn red or yellow. Grows in woodland edges, often moist.",
            "de": "Blätter rund mit langen, abgeflachten Stielen – sie zittern schon bei leichtem Wind. Rinde glatt, graugrün, mit rautenförmigen 'Augen'. Im Herbst rot oder gelb. Wächst an Waldrändern.",
            "fr": "Feuilles rondes à longs pétioles aplatis – elles tremblent au moindre vent. Écorce lisse, gris-vert, avec des 'yeux' en losange. En automne rouges ou jaunes. Pousse en lisière de bois.",
            "es": "Hojas redondeadas con pecíolos largos y aplanados – tiemblan con una brisa ligera. Corteza lisa, gris-verde, con 'ojos' rómbicos. En otoño rojas o amarillas. Crece en bordes de bosque.",
            "uk": "Листки округлі, з довгими пласкими черешками – тремтять навіть від легкого вітерцю. Кора гладенька, сіро-зелена, з ромбічними 'вічками'. Восени червоні або жовті. Росте на узліссях.",
        },
    },
    "Prunus padus": {
        "names": {"lt": "Paprastoji ieva", "en": "Bird cherry", "de": "Gewöhnliche Traubenkirsche",
                   "fr": "Merisier à grappes", "es": "Cerezo de racimo", "uk": "Черемха звичайна"},
        "desc": {
            "lt": "Lapai pailgi, smulkiai dantyti, tamsiai žali. Pavasarį ieva pasipuošia ilgomis, kabančiomis, stipriai kvepiančiomis baltų žiedų kekėmis – jų kvapą pajusi dar prieš pamatydamas medį. Vaisiai – smulkios, juodos uogos. Auga drėgnose, derlingose dirvose.",
            "en": "Leaves are oblong, finely toothed, dark green. In spring the bird cherry dresses up with long, drooping, intensely fragrant white flower racemes – you'll smell them before you see the tree. Fruits are small black berries. Grows on moist, fertile soils.",
            "de": "Blätter länglich, fein gezähnt, dunkelgrün. Im Frühling lange, hängende, stark duftende weiße Blütentrauben. Früchte kleine schwarze Beeren. Wächst auf feuchten, fruchtbaren Böden.",
            "fr": "Feuilles oblongues, finement dentées, vert foncé. Au printemps, longues grappes pendantes de fleurs blanches intensément parfumées. Fruits : petites baies noires. Pousse sur des sols humides et fertiles.",
            "es": "Hojas oblongas, finamente dentadas, verde oscuro. En primavera, largos racimos colgantes de flores blancas intensamente fragantes. Frutos: pequeñas bayas negras. Crece en suelos húmedos y fértiles.",
            "uk": "Листки довгасті, дрібнозубчасті, темно-зелені. Навесні довгі пониклі суцвіття білих квітів із сильним ароматом. Плоди – дрібні чорні ягоди. Росте на вологих родючих ґрунтах.",
        },
    },
    "Pyrus pyraster": {
        "names": {"lt": "Miškinė kriaušė", "en": "European wild pear", "de": "Wildbirne",
                   "fr": "Poirier sauvage", "es": "Peral silvestre", "uk": "Груша лісова"},
        "desc": {
            "lt": "Panaši į miškinę obelį, bet vaisiai kietesni, smulkūs, tikros kriaušės formos. Šakelės su aštriais dygliais. Lapai blizgūs, apvaliai kiaušiniški, smulkiai dantyti. Žiedai balti, žydi balandį–gegužę. Auga sausose, kalkingose dirvose.",
            "en": "Similar to the wild apple but with harder, smaller fruits of true pear shape. Twigs bear sharp thorns. Leaves are glossy, roundly ovate, finely toothed. Flowers are white, blooming April–May. Grows on dry, calcareous soils.",
            "de": "Ähnlich dem Holzapfel, aber mit härteren, kleineren Früchten in echter Birnenform. Zweige mit scharfen Dornen. Blätter glänzend, rundlich-eiförmig. Blüten weiß, April–Mai. Wächst auf trockenen, kalkhaltigen Böden.",
            "fr": "Semblable au pommier sauvage, mais aux fruits plus durs, plus petits, de vraie forme de poire. Rameaux à épines acérées. Feuilles luisantes, arrondies-ovales. Fleurs blanches, avril–mai. Pousse sur des sols secs et calcaires.",
            "es": "Similar al manzano silvestre pero con frutos más duros, pequeños, de auténtica forma de pera. Ramillas con espinas afiladas. Hojas brillantes, ovalado-redondeadas. Flores blancas, abril–mayo. Crece en suelos secos y calcáreos.",
            "uk": "Схожа на яблуню лісову, але плоди твердіші, дрібні, справжньої грушоподібної форми. Пагони з гострими колючками. Листки блискучі, округло-яйцеподібні. Квіти білі, квітень–травень. Росте на сухих вапняних ґрунтах.",
        },
    },
    "Quercus petraea": {
        "names": {"lt": "Bekotis ąžuolas", "en": "Sessile oak", "de": "Traubeneiche",
                   "fr": "Chêne sessile", "es": "Roble albar", "uk": "Дуб скельний"},
        "desc": {
            "lt": "Panašus į paprastąjį ąžuolą, bet lapai turi aiškų kotelį, o gilės – be jo, sėdi tiesiai ant šakelės. Lapų skiltys lygesnės, lapai šiek tiek odiškesni. Auga sausesnėse, dažnai kalvotose vietose. Mediena labai vertinama.",
            "en": "Similar to English oak, but leaves have a clear petiole and acorns sit directly on the twig without a stalk. Leaf lobes are more regular, leaves slightly more leathery. Grows on drier, often hilly sites. Its timber is highly prized.",
            "de": "Ähnlich der Stieleiche, aber die Blätter haben einen deutlichen Stiel und die Eicheln sitzen ohne Stiel direkt am Zweig. Blattlappen regelmäßiger. Wächst an trockeneren, oft hügeligen Standorten.",
            "fr": "Semblable au chêne pédonculé, mais les feuilles ont un pétiole net et les glands sont sessiles, directement sur le rameau. Lobes foliaires plus réguliers. Pousse sur des sites plus secs, souvent vallonnés.",
            "es": "Similar al roble común, pero las hojas tienen un pecíolo claro y las bellotas se sientan directamente sobre la ramilla. Lóbulos más regulares. Crece en lugares más secos, a menudo colinares.",
            "uk": "Схожий на дуб звичайний, але листки мають виразний черешок, а жолуді сидять без нього, прямо на пагоні. Лопаті листків рівніші. Росте на сухіших, часто пагорбистих місцях.",
        },
    },
    "Quercus robur": {
        "names": {"lt": "Paprastasis ąžuolas", "en": "English oak", "de": "Stieleiche",
                   "fr": "Chêne pédonculé", "es": "Roble común", "uk": "Дуб звичайний"},
        "desc": {
            "lt": "Lapai su apvaliomis skiltimis, beveik bekociai – tarsi žalios bangos. Žievė giliai sueižėjusi, tamsiai ruda, laikui bėgant tampa tarsi šarvai. Gilės su dubenėliu, išsidėsčiusios ant ilgo kotelio. Ilgaamžis milžinas, galintis gyventi 500–1000 metų – tikras miško karalius.",
            "en": "Leaves with rounded lobes, almost sessile – like green waves. Bark deeply fissured, dark brown, becoming like armour over time. Acorns sit in a cup on a long stalk. A long-lived giant, able to reach 500–1000 years – a true king of the forest.",
            "de": "Blätter mit gerundeten Lappen, fast sitzend – wie grüne Wellen. Rinde tief gefurcht, dunkelbraun, wird wie eine Rüstung. Eicheln in einem Becher an langem Stiel. Ein langlebiger Riese, kann 500–1000 Jahre alt werden.",
            "fr": "Feuilles à lobes arrondis, presque sessiles – comme des vagues vertes. Écorce profondément fissurée, brun foncé, devenant comme une armure. Glands dans une cupule sur un long pédoncule. Un géant pouvant atteindre 500 à 1000 ans.",
            "es": "Hojas con lóbulos redondeados, casi sésiles – como olas verdes. Corteza profundamente agrietada, marrón oscuro. Bellotas en una cúpula sobre un largo pedúnculo. Un gigante capaz de alcanzar los 500–1000 años.",
            "uk": "Листки з округлими лопатями, майже сидячі – наче зелені хвилі. Кора глибоко потріскана, темно-бура. Жолуді в плюсці на довгому черешку. Довговічний велетень, здатний прожити 500–1000 років.",
        },
    },
    "Salix alba": {
        "names": {"lt": "Baltasis gluosnis", "en": "White willow", "de": "Silber-Weide",
                   "fr": "Saule blanc", "es": "Sauce blanco", "uk": "Верба біла"},
        "desc": {
            "lt": "Lapai pailgi, sidabriškai žali, ypač apatinė pusė, su šilkiniais plaukeliais – lyg būtų apibarstyti miltais. Šakelės lanksčios, geltonos arba rausvos. Auga prie vandens, upių ir ežerų pakrantėse. Dažnai naudojamas kaip dekoratyvus medis.",
            "en": "Leaves are long, silvery-green – especially beneath – with silky hairs, as if dusted with flour. Twigs are flexible, yellow or reddish. Grows by water, along rivers and lake shores. Often planted as an ornamental tree.",
            "de": "Blätter lang, silbrig-grün – besonders unterseits – mit seidigen Haaren, wie bemehlt. Zweige biegsam, gelb oder rötlich. Wächst am Wasser. Oft als Zierbaum gepflanzt.",
            "fr": "Feuilles longues, vert argenté – surtout dessous – aux poils soyeux, comme saupoudrées de farine. Rameaux souples, jaunes ou rougeâtres. Pousse au bord de l'eau. Souvent planté comme ornement.",
            "es": "Hojas largas, verde plateado – sobre todo por el envés – con pelos sedosos, como enharinadas. Ramillas flexibles, amarillas o rojizas. Crece junto al agua. A menudo plantado como ornamental.",
            "uk": "Листки довгі, сріблясто-зелені – особливо знизу – з шовковистими волосками, наче припудрені борошном. Пагони гнучкі, жовті або червоняві. Росте біля води. Часто висаджують як декоративне дерево.",
        },
    },
    "Salix caprea": {
        "names": {"lt": "Blindė", "en": "Goat willow", "de": "Sal-Weide",
                   "fr": "Saule marsault", "es": "Sauce cabruno", "uk": "Верба козяча"},
        "desc": {
            "lt": "Stambūs, platūs, apvalūs lapai su raukšlėtu, šiek tiek plaukuotu paviršiumi. Pavasarį – dideli, pilki, pūkiniai „kačiukai“ (žiedynai), kuriuos mėgsta bitės ir vaikai. Krūmas arba mažas medis. Auga miškų pakraščiuose ir pagrioviuose, vienas pirmųjų pasitinka pavasarį.",
            "en": "Large, broad, rounded leaves with a wrinkled, slightly hairy surface. In spring it bears large grey, downy catkins, beloved by bees and children. A shrub or small tree. Grows on woodland edges and ditches – one of the first to greet spring.",
            "de": "Große, breite, runde Blätter mit runzliger Oberfläche. Im Frühling große graue, flauschige Kätzchen, geliebt von Bienen und Kindern. Ein Strauch oder kleiner Baum. Wächst an Waldrändern und Straßengräben.",
            "fr": "Grandes feuilles larges et arrondies à surface ridée. Au printemps, gros chatons gris et duveteux, aimés des abeilles et des enfants. Un arbuste ou petit arbre. Pousse en lisière de bois et dans les fossés.",
            "es": "Hojas grandes, anchas y redondeadas, con superficie arrugada. En primavera, grandes amentos grises y vellosos, amados por abejas y niños. Un arbusto o pequeño árbol. Crece en bordes de bosque y cunetas.",
            "uk": "Великі, широкі, округлі листки зі зморшкуватою поверхнею. Навесні – великі сірі пухнасті 'котики', які люблять бджоли й діти. Кущ або невелике дерево. Росте на узліссях і в кюветах.",
        },
    },
    "Salix fragilis": {
        "names": {"lt": "Trapusis gluosnis", "en": "Crack willow", "de": "Bruch-Weide",
                   "fr": "Saule fragile", "es": "Mimbrera frágil", "uk": "Верба ламка"},
        "desc": {
            "lt": "Labai panašus į baltąjį gluosnį, bet šakelės lengvai lūžta – iš čia ir „trapusis“ vardas. Lapai blizgūs, plonesni, ryškiai žali, be šilkinio plaukelio. Auga prie vandens, dažnai šalia baltųjų gluosnių. Dažnai kryžminasi su baltuoju gluosniu.",
            "en": "Very similar to white willow but its twigs snap easily – hence the name, you can hear a loud crack. Leaves are glossy, thinner, bright green. Grows by water, often alongside white willows. Frequently hybridises with white willow.",
            "de": "Sehr ähnlich der Silber-Weide, aber ihre Zweige brechen leicht – daher der Name. Blätter glänzend, dünner, hellgrün. Wächst am Wasser, oft neben Silber-Weiden. Hybridisiert häufig mit der Silber-Weide.",
            "fr": "Très semblable au saule blanc, mais ses rameaux cassent facilement – d'où son nom. Feuilles luisantes, plus fines, vert vif. Pousse au bord de l'eau, souvent aux côtés de saules blancs. S'hybride fréquemment.",
            "es": "Muy similar al sauce blanco, pero sus ramillas se rompen con facilidad – de ahí su nombre. Hojas brillantes, más finas, verde brillante. Crece junto al agua, a menudo junto a sauces blancos. Se hibrida con frecuencia.",
            "uk": "Дуже схожа на вербу білу, але її пагони легко ламаються – звідси й назва. Листки блискучі, тонші, яскраво-зелені. Росте біля води, часто поряд із вербами білими. Часто гібридизується.",
        },
    },
    "Sorbus aucuparia": {
        "names": {"lt": "Paprastasis šermukšnis", "en": "Rowan", "de": "Vogelbeere",
                   "fr": "Sorbier des oiseleurs", "es": "Serbal de los cazadores", "uk": "Горобина звичайна"},
        "desc": {
            "lt": "Lapai sudėtiniai, su 11–15 lapelių – atrodo tarsi žalios plunksnos. Žievė lygi, pilka, su skersinėmis žymėmis. Pavasarį žydi baltais žiedais, o rudenį prinoksta oranžinės uogos, sukabintos kekėmis – jų negali nepastebėti. Auga miškuose, dažnai prie kelių ir miško aikštelių.",
            "en": "Leaves are pinnate with 11–15 leaflets – they look like green feathers. Bark is smooth and grey. Flowers are white in spring, and orange berries ripen in autumn in bright clusters – impossible to miss. Grows in woods, often along roads and clearings.",
            "de": "Blätter gefiedert mit 11–15 Fiederblättchen – wie grüne Federn. Rinde glatt, grau. Blüten weiß im Frühling, im Herbst orange Beeren in leuchtenden Doldentrauben. Wächst in Wäldern, oft an Wegen.",
            "fr": "Feuilles composées pennées à 11–15 folioles – comme des plumes vertes. Écorce lisse, grise. Fleurs blanches au printemps, baies orange en grappes éclatantes en automne. Pousse dans les bois, souvent au bord des routes.",
            "es": "Hojas compuestas pinnadas con 11–15 foliolos – parecen plumas verdes. Corteza lisa y gris. Flores blancas en primavera, bayas naranjas en vistosos racimos en otoño. Crece en bosques, a menudo junto a caminos.",
            "uk": "Листки складні, пірчасті, з 11–15 листочками – наче зелені пера. Кора гладенька, сіра. Квіти білі навесні, а восени оранжеві ягоди у яскравих гронах. Росте в лісах, часто обабіч доріг.",
        },
    },
    "Taxus baccata": {
        "names": {"lt": "Europinis kukmedis", "en": "European yew", "de": "Europäische Eibe",
                   "fr": "If commun", "es": "Tejo común", "uk": "Тис ягідний"},
        "desc": {
            "lt": "Amžinai žalias medis su plokščiais, 2–3 cm spygliukais – apačioje jie turi dvi šviesias juostas. Sėklos – su ryškiai raudonu, minkštu gaubtu, kuris atrodo kaip uoga. Auga pavėsyje, labai ilgaamžis, gali gyventi net 2000 metų – tikras ilgaamžiškumo rekordininkas.",
            "en": "An evergreen tree with flat needles 2–3 cm long – they have two pale bands on the underside. Seeds sit in a bright red fleshy aril that looks like a berry. Grows in shade; extremely long-lived, can reach 2000 years.",
            "de": "Ein immergrüner Baum mit flachen Nadeln, 2–3 cm lang – unterseits mit zwei hellen Streifen. Samen in einem leuchtend roten fleischigen Arillus. Wächst im Schatten; extrem langlebig, bis 2000 Jahre.",
            "fr": "Un arbre toujours vert à aiguilles plates de 2–3 cm – avec deux bandes claires dessous. Les graines sont logées dans un arille charnu rouge vif. Pousse à l'ombre ; extrêmement longévif, jusqu'à 2000 ans.",
            "es": "Un árbol perennifolio con acículas planas de 2–3 cm – con dos bandas claras en el envés. Las semillas están envueltas en un arilo carnoso rojo brillante. Crece en la sombra; extremadamente longevo, hasta 2000 años.",
            "uk": "Вічнозелене дерево з плоскими голками 2–3 см – знизу вони мають дві світлі смуги. Насіння оточене яскраво-червоним м'ясистим принасінником. Росте в тіні; надзвичайно довговічне, до 2000 років.",
        },
    },
    "Tilia cordata": {
        "names": {"lt": "Mažalapė liepa", "en": "Small-leaved lime", "de": "Winter-Linde",
                   "fr": "Tilleul à petites feuilles", "es": "Tilo de hoja pequeña", "uk": "Липа дрібнолиста"},
        "desc": {
            "lt": "Lapai širdiški, smulkiai dantyti, su ryškiomis gyslomis, apatinė pusė melsvai žalia. Žiedai gelsvi, labai kvapnūs, su lapeliu-priedu – jų kvapas liepą paverčia tikru bičių rojumi. Žydi liepą, medingas. Auga derlingose, drėgnose dirvose, dažna parkuose ir prie namų.",
            "en": "Leaves are heart-shaped, finely toothed, with prominent veins and a bluish-green underside. Flowers are pale yellow, very fragrant, with a leafy bract – their scent turns July into a bee paradise. Blooms in July, highly melliferous.",
            "de": "Blätter herzförmig, fein gezähnt, mit ausgeprägten Adern. Blüten blassgelb, sehr duftend, mit einem Hochblatt – ihr Duft macht den Juli zum Bienenparadies. Blüht im Juli, stark honiggebend.",
            "fr": "Feuilles cordiformes, finement dentées, aux nervures marquées. Fleurs jaune pâle, très parfumées, avec une bractée – leur parfum transforme juillet en paradis des abeilles. Floraison en juillet, très mellifère.",
            "es": "Hojas acorazonadas, finamente dentadas, con nervios marcados. Flores amarillo pálido, muy fragantes, con una bráctea – su aroma convierte julio en un paraíso para las abejas. Florece en julio, muy melífera.",
            "uk": "Листки серцеподібні, дрібнозубчасті, з виразними жилками. Квіти блідо-жовті, дуже запашні, з листоподібним приквітком – їхній аромат перетворює липень на бджолиний рай. Цвіте в липні, добрий медонос.",
        },
    },
    "Ulmus glabra": {
        "names": {"lt": "Kalninė guoba", "en": "Wych elm", "de": "Bergulme",
                   "fr": "Orme de montagne", "es": "Olmo de montaña", "uk": "В'яз гірський"},
        "desc": {
            "lt": "Dideli, šiurkštūs lapai su nelygiu, dvigubu pamatu. Vaisiai – plokšti, sparnuoti riešutėliai, sukabinti kekėmis, subręsta dar pavasarį. Žievė ilgai lieka lygi, vėliau sueižėja. Auga derlingose, drėgnose dirvose, dažna mišriuose miškuose.",
            "en": "Large, rough leaves with an unequal, doubly serrate base. Fruits are flat, winged samaras clustered in bunches, ripening in spring. Bark stays smooth for a long time, later fissuring. Grows on fertile, moist soils, common in mixed woodland.",
            "de": "Große, raue Blätter mit ungleicher, doppelt gesägter Basis. Früchte flache, geflügelte Spaltfrüchte in Büscheln, reifen im Frühling. Rinde bleibt lange glatt. Wächst auf fruchtbaren, feuchten Böden.",
            "fr": "Grandes feuilles rugueuses à base inégale et doublement dentée. Fruits plats et ailés, en bouquets, mûrissant au printemps. L'écorce reste longtemps lisse. Pousse sur des sols fertiles et humides.",
            "es": "Hojas grandes y ásperas con base desigual y doblemente aserrada. Frutos planos y alados, en racimos, maduran en primavera. La corteza permanece lisa mucho tiempo. Crece en suelos fértiles y húmedos.",
            "uk": "Великі шорсткі листки з нерівною, двічі пилчастою основою. Плоди – плоскі крилаті двосім'янки в пучках, достигають навесні. Кора довго гладенька. Росте на родючих вологих ґрунтах.",
        },
    },
    "Ulmus laevis": {
        "names": {"lt": "Paprastoji vinkšna", "en": "European white elm", "de": "Flatterulme",
                   "fr": "Orme lisse", "es": "Olmo temblón", "uk": "В'яз гладкий"},
        "desc": {
            "lt": "Panaši į guobą, bet lapai lygesni, mažiau šiurkštūs, pamatas simetriškesnis. Vaisiai – sparnuoti, su blakstienėlėmis palei kraštą, sukabinti ilgais koteliais. Žievė pilkai ruda, sueižėjusi. Auga drėgnose, derlingose dirvose, dažna prie upių.",
            "en": "Similar to wych elm, but leaves are smoother and more symmetrical at the base. Fruits are winged with ciliate margins, hanging from long stalks. Bark is grey-brown, fissured. Grows in moist, fertile soils, common near rivers.",
            "de": "Ähnlich der Bergulme, aber Blätter glatter, symmetris
