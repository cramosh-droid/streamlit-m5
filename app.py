import streamlit as st
import pandas as pd 
from PIL import Image
logo_pestana = Image.open("logo.png")

st.set_page_config(
    page_title="Dashboard Capital Humano",
    page_icon=logo_pestana,
    layout="wide",
)
#logo centrado
col1, col2, col3 = st.columns ([2, 2, 2])
with col2:
    st.image("logo.png", width=200)

# titulo
st.markdown("<h1 style='text-align: center;'>Dashboard Capital Humano</h1>",
unsafe_allow_html=True
)
# Descripcion
st.markdown(
    """
    Bienvenido al Dashboard de Capital Humano!
    Esta herramienta fue creada con la finalidad de poder esplorar el talento interno de nuestra empresa.
    Aqui observaras indicadores claves para el desarrollo de nuestros colaboradores!
    """
)
st.divider()
