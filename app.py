import streamlit as st
import pandas as pd
import altair as alt

st.title('Exportaciones no petroleras de Ecuador a Estados Unidos')


df_tradicionales = pd.read_csv('dataset_tradicionales.csv')
df_no_tradicionales = pd.read_csv('dataset_noTradicionales.csv')

year = st.slider('Año', min_value=2001, max_value=2021, value=2001, step=1)

tradi = pd.read_csv('tradicionales.csv')
tradi = tradi[tradi['Año'] == year]

no_tradi = pd.read_csv('no_tradicionales.csv')
no_tradi = no_tradi[no_tradi['Año'] == year]

tradicionales_por_mes = pd.read_csv('tradicionales_total.csv')
tradicionales_por_mes = tradicionales_por_mes[tradicionales_por_mes['Año']==year]

no_tradicionales_por_mes = pd.read_csv('no_tradicionales_total.csv')
no_tradicionales_por_mes = no_tradicionales_por_mes[no_tradicionales_por_mes['Año']==year]

tradicionales = df_tradicionales[df_tradicionales['Año'] == year]
no_tradicionales = df_no_tradicionales[df_no_tradicionales['Año'] == year]


tradicionales_total = tradicionales['Toneladas'].sum()
no_tradicionales_total = no_tradicionales['Toneladas'].sum()

st.header('Indicadores anuales')
col1, col2, col3 = st.columns(3)
col1.metric("Productos tradicionales", f"{round(tradicionales_total, 2)} t")
col2.metric("Productos no tradicionales", f"{round(no_tradicionales_total, 2)} t")

df = pd.DataFrame({'Categoría': ['Tradicional', 'No tradicional'], 'Toneladas': [tradicionales_total, no_tradicionales_total]})

with col3:
    bar = alt.Chart(df).mark_bar().encode(y='Categoría', x='Toneladas', tooltip = ['Categoría', 'Toneladas']).properties(width = 250).interactive()
    st.altair_chart(bar)

st.header('Exportaciones totales')

line1 = alt.Chart(tradicionales_por_mes).mark_line(color="Orange").encode(
    x = 'Mes',
    y = 'Toneladas',
    tooltip = ['Mes', 'Toneladas']
).properties(title = "Productos tradicionales", width = 650)

st.altair_chart(line1)

line2 = alt.Chart(no_tradicionales_por_mes).mark_line(color="Green").encode(
    x = 'Mes',
    y = 'Toneladas',
    tooltip = ['Mes', 'Toneladas']
).properties(title = "Productos no tradicionales", width = 650)

st.altair_chart(line2)

st.header('Exportaciones por producto')

st.markdown('##### Productos tradicionales')

valores = tradicionales['Producto']
seleccion = st.selectbox('Elija un producto:',valores)

line3 = alt.Chart(tradi[tradi['Producto'] == seleccion]).mark_line().encode(
    x = 'Mes',
    y = 'Toneladas',
    tooltip = ['Mes', 'Toneladas']
).properties(width = 650)

st.altair_chart(line3)

st.markdown('##### Productos no tradicionales')

valores2 = no_tradicionales['Producto']
seleccion2 = st.selectbox('Elija un producto:',valores2)

line4 = alt.Chart(no_tradi[no_tradi['Producto'] == seleccion2]).mark_line(color="Red").encode(
    x = 'Mes',
    y = 'Toneladas',
    tooltip = ['Mes', 'Toneladas']
).properties(width = 650)

st.altair_chart(line4)