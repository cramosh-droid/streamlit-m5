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

#selector en barra lateral de genero
genero_seleccionado = st.sidebar.selectbox("Selecciona el Genero:",
options=["Todos"] + list(df['gender'].unique())
)

#selector estado civil
estado_civil = st.sidebar.selectbox(
    "selecciona el estado Civil:",
    options = ["Todos"] + list(df['marital_status'].unique())
)

#deslizante de desempeño
rango_desempeno = st.sidebar.slider(
    "seleccione el rango de desempeño:",
    min_value=1,
    max_value=5,
    value=(1,5)
)
puntaje_min = rango_desempeno[0]
puntaje_max = rango_desempeno[1]


#Data frame filtrado
df_filtrado = df.copy()
#Filtro genero
if genero_seleccionado != "Todos":
    df_filtrado = df_filtrado[df_filtrado['gender']==genero_seleccionado]
#Filtro estado civil
if estado_civil != "Todos":
    df_filtrado = df_filtrado[df_filtrado['marital_status'] == estado_civil]
#Filtro Rango de desempeño
df_filtrado = df_filtrado[
    (df_filtrado['performance_score'] >= rango_desempeno[0]) &
    (df_filtrado ['performance_score'] <= rango_desempeno[1])
]

# Grafica de dona para ver la comparativa entre generos
st.subheader("Distribucion de Colaboradores por genero")
conteo_genero = df_filtrado['gender'].value_counts().reset_index()
conteo_genero.columns = ['Genero', 'Cantidad']

import plotly.express as px
fig_genero = px.pie(
    conteo_genero,
    values='Cantidad',
    names='Genero',
    color='Genero',
    color_discrete_map={'M': '#3a86ff', 'F': '#e377c2'},
    hole=0.4
)
fig_genero.update_traces(textinfo='percent+label')
fig_genero.update_layout(showlegend=False)



#Histograma para distribucion de desempeño
fig_desempeno = px.histogram(
    df_filtrado,
    x= 'performance_score',
    title= "Distribucion de los puntajes de Desempeño",
    labels={'performance_score':'Puntaje de Desempeño', 'count' : 'Cantidad de Empleados '},
    color_discrete_sequence=['orchid']
)
fig_desempeno.update_layout(bargap=0.2)
fig_desempeno.update_xaxes(tickmode='linear',tick0=1,dtick=1)

#Acomodo de grafica de dona e histrograma
col1, col2 = st.columns(2)
with col1:
    st.subheader("Genero de Empleado")
    st.plotly_chart(fig_genero, use_container_width=True)
with col2:
    st.subheader("Distribucion de Desempeño")
    st.plotly_chart(fig_desempeno, use_container_width=True)

st.markdown("---")
#Grafica de barras para ver las horas promedio por genero
df_promedio_horas = df_filtrado.groupby('gender')['average_work_hours'].mean().reset_index()
fig_horas =px.bar(
    df_promedio_horas,
    x='gender',
    y='average_work_hours',
    title="Promedio de Horas trabajadas por Genero",
    labels={'gender':'Genero','average_work_hours':'Promedio de horas'},
    color='gender',
    color_discrete_map={'M':'#3a86ff', 'F': '#e377c2'}
)
st.plotly_chart(fig_horas,use_container_width=True)
st.markdown("---")
# Scatter plot para ver salario vs edad
fig_salario_vs_edad = px.scatter(
    df_filtrado,
    x='age',
    y='salary',
    title="Relacion entre Edad y Salario de los Colaboradores",
    labels={'age':'Edad','salary':'Compensacion ($)'},
    color='gender',
    color_discrete_map={'M': '#3a86ff', 'F': '#e377c2'},
    hover_data=['performance_score']
)
st.plotly_chart(fig_salario_vs_edad, use_container_width = True)

st.markdown("---")

#Grafica de boxplot para ver la relacion entre puntaje de desempeño vs horas trabajadas
fig_puntaje_vs_horas = px.box(
    df_filtrado,
    x='performance_score',
    y='average_work_hours',
    title = "Relacion entre Horas Trabajadas y Puntaje de Desempeño",
    labels = {'performance_score':'Puntaje de desempeño', 'average_work_hours':'Promedio de horas Trabajadas'},
    color = 'performance_score',
    points ='outliers'
)
st.plotly_chart(fig_puntaje_vs_horas, use_container_width = True)