import streamlit as st
import pandas as pd 
from PIL import image
logo_pestana = image.open("logo.png")

st.set_page_config(
    page_title="Dashboard Capital Humano",
    page_icon=logo_pestana,
    layout="wide",
)
# Codigo de logo
st.image("logo.png", width=200)

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
