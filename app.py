import streamlit as st
from textblob import TextBlob
from googletrans import Translator
from streamlit_lottie import st_lottie
import json

# Configuración de la página
st.set_page_config(page_title="Análisis de Sentimientos", page_icon="😊", layout="centered")
translator = Translator()

# Estilos personalizados
st.markdown(
    """
    <style>
    .title {
        text-align: center;
        color: #2E86C1;
        font-size: 40px;
        font-weight: bold;
    }
    .subheader {
        color: #117864;
        font-size: 20px;
        font-weight: bold;
    }
    .result {
        font-size: 18px;
        font-weight: bold;
        padding: 10px;
        border-radius: 10px;
        text-align: center;
    }
    .positive {
        background-color: #D4EFDF;
        color: #1D8348;
    }
    .negative {
        background-color: #FADBD8;
        color: #C0392B;
    }
    .neutral {
        background-color: #D5DBDB;
        color: #2C3E50;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Título principal
st.markdown('<div class="title">Análisis de Sentimientos</div>', unsafe_allow_html=True)

# Sección de instrucciones
st.subheader("📌 Escribe una frase para analizar su sentimiento")

# Análisis de polaridad y subjetividad
with st.expander("📊 Analizar Polaridad y Subjetividad"):
    text1 = st.text_area("✍️ Ingresa el texto aquí:")
    if text1:
        translation = translator.translate(text1, src="es", dest="en")
        trans_text = translation.text
        blob = TextBlob(trans_text)
        polarity = round(blob.sentiment.polarity, 2)
        subjectivity = round(blob.sentiment.subjectivity, 2)
        
        # Mostrar los resultados
        st.markdown(f"**Polaridad:** `{polarity}`")
        st.markdown(f"**Subjetividad:** `{subjectivity}`")
        
        if polarity >= 0.5:
            st.markdown('<div class="result positive">😊 Sentimiento Positivo</div>', unsafe_allow_html=True)
        elif polarity <= -0.5:
            st.markdown('<div class="result negative">😔 Sentimiento Negativo</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="result neutral">😐 Sentimiento Neutral</div>', unsafe_allow_html=True)

# Corrección de texto en inglés
with st.expander("✏️ Corrección en inglés"):
    text2 = st.text_area("✍️ Ingresa el texto en inglés:", key='4')
    if text2:
        blob2 = TextBlob(text2)
        corrected_text = blob2.correct()
        st.markdown(f"**Texto corregido:** `{corrected_text}`")

# Animación Lottie
with open('Animation - 1741878051974.json') as source:
    animation = json.load(source)
st_lottie(animation, width=350)

