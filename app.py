import streamlit as st
import pandas as pd
import altair as alt

st.title('Exportaciones no petroleras de Ecuador a Estados Unidos')

trad_tipo_mes = pd.read_csv('./data/trad_tipo_mes.csv')
no_trad_tipo_mes = pd.read_csv('./data/no_trad_tipo_mes.csv')

trad_total_mes = pd.read_csv('./data/trad_total_mes.csv')
no_trad_total_mes = pd.read_csv('./data/no_trad_total_mes.csv')

year = st.slider('Año', min_value=2001, max_value=2021, value=2001, step=1)

trad_tipo_mes = trad_tipo_mes[trad_tipo_mes['Año'] == year]
no_trad_tipo_mes = no_trad_tipo_mes[no_trad_tipo_mes['Año'] == year]

no_trad_total_mes = no_trad_total_mes[no_trad_total_mes['Año'] == year]
trad_total_mes = trad_total_mes[trad_total_mes['Año'] == year]

tradicionales_total = trad_total_mes['Toneladas'].sum()
no_tradicionales_total = no_trad_total_mes['Toneladas'].sum()

st.header('Indicadores anuales')
col1, col2, col3 = st.columns(3)
col1.metric("Productos tradicionales", f"{round(tradicionales_total, 2)} t")
col2.metric("Productos no tradicionales", f"{round(no_tradicionales_total, 2)} t")

df = pd.DataFrame({'Categoría': ['Tradicional', 'No tradicional'], 'Toneladas': [tradicionales_total, no_tradicionales_total]})

with col3:
    bar = alt.Chart(df).mark_bar().encode(y='Categoría', x='Toneladas', tooltip = ['Categoría', 'Toneladas']).properties(width = 250).interactive()
    st.altair_chart(bar)

st.header('Exportaciones totales')

line1 = alt.Chart(trad_total_mes).mark_line(color="Orange").encode(
    x = 'Mes',
    y = 'Toneladas',
    tooltip = ['Mes', 'Toneladas']
).properties(title = "Productos tradicionales", width = 650)

st.altair_chart(line1)

line2 = alt.Chart(no_trad_total_mes).mark_line(color="Green").encode(
    x = 'Mes',
    y = 'Toneladas',
    tooltip = ['Mes', 'Toneladas']
).properties(title = "Productos no tradicionales", width = 650)

st.altair_chart(line2)

st.header('Exportaciones por producto')

st.markdown('##### Productos tradicionales')

valores = set(trad_tipo_mes['Producto'].to_list())
seleccion = st.selectbox('Elija un producto:',valores)

line3 = alt.Chart(trad_tipo_mes[trad_tipo_mes['Producto'] == seleccion]).mark_line().encode(
    x = 'Mes',
    y = 'Toneladas',
    tooltip = ['Mes', 'Toneladas']
).properties(width = 650)

st.altair_chart(line3)

st.markdown('##### Productos no tradicionales')

valores2 = set(no_trad_tipo_mes['Producto'].to_list())
seleccion2 = st.selectbox('Elija un producto:',valores2)

line4 = alt.Chart(no_trad_tipo_mes[no_trad_tipo_mes['Producto'] == seleccion2]).mark_line(color="Red").encode(
    x = 'Mes',
    y = 'Toneladas',
    tooltip = ['Mes', 'Toneladas']
).properties(width = 650)

st.altair_chart(line4)