import streamlit as st
import pandas as pd 
from PIL import Image
logo_pestana = Image.open("logo.png")

#logo en pestaña de internet y nombre de pagina
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
    Esta herramienta fue creada con la finalidad de poder explorar el talento interno de nuestra empresa.
    Aqui observaras indicadores claves para el desarrollo de nuestros colaboradores!
    """
)
st.divider()
#llamado de archivo y mensaje de error en caso de no encontrarlo
try: 
    df = pd.read_csv("Employee_data.csv")
except FileNotFoundError:
    st.error("No se encontro el archivo 'Employee_data.csv")
    st.stop()

#selector en barra lateral
genero_seleccionado = st.sidebar.selectbox("Selecciona el Genero:",
options=["Todos"] + list(df['gender'].unique())
)

# Grafica de dona
st.subheader("Distribucion de Colaboradores por genero")
conteo_genero = df['gender'].value_counts().reset_index()
conteo_genero.columns = ['Genero', 'Cantidad']

import plotly.express as px
fig_genero = px.pie(
    conteo_genero,
    values='Cantidad',
    names='Genero',
    color='Genero',
    color_discrete_map={'M': '#1f77b4', 'F': '#e377c2'},
    hole=0.4
)
fig_genero.update_traces(textinfo='percent+label')
fig_genero.update_layout(showlegend=False)

st.plotly_chart(fig_genero, use_container_width=True)