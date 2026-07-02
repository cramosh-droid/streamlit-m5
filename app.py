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
st.markdown(
    "<div style='text-align: center;'><img src='app/static/logo.png' width='200'></div>",
    unsafe_allow_html=True
)

# titulo
st.title("Dashboard Capital Humano")
# Descripcion
st.markdown(
    """
    Bienvenido al Dashboard de Capital Humano!
    Esta herramienta fue creada con la finalidad de poder esplorar el talento interno de nuestra empresa.
    Aqui observaras indicadores claves para el desarrollo de nuestros colaboradores!
    """
)
st.divider()
