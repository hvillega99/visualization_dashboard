import streamlit as st
import pandas as pd
import altair as alt

meses = {1: "Enero", 2:"Febrero", 3:"Marzo", 4:"Abril", 5:"Mayo", 
        6:"Junio", 7:"Julio", 8:"Agosto", 9:"Septiembre", 10:"Octubre", 
        11:"Noviembre", 12:"Diciembre"}

def replace(num_mes):
    return meses[num_mes]

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

trad_tipo_mes['Mes'] = trad_tipo_mes['Mes'].apply(replace)
no_trad_tipo_mes['Mes'] = no_trad_tipo_mes['Mes'].apply(replace)
no_trad_total_mes['Mes'] = no_trad_total_mes['Mes'].apply(replace)
trad_total_mes['Mes'] = trad_total_mes['Mes'].apply(replace)

tradicionales_total = trad_total_mes['Toneladas'].sum()
no_tradicionales_total = no_trad_total_mes['Toneladas'].sum()

st.header('Indicadores anuales')
col1, col2, col3 = st.columns(3)
col1.metric("Productos tradicionales", f" {'{:,}'.format(round(tradicionales_total, 2)).replace(',', ' ')} t")
col2.metric("Productos no tradicionales", f" {'{:,}'.format(round(no_tradicionales_total, 2)).replace(',', ' ')} t")

df = pd.DataFrame({'Categoría': ['Tradicional', 'No tradicional'], 'Toneladas': [tradicionales_total, no_tradicionales_total]})

with col3:
    pieAlt = alt.Chart(df).mark_arc().encode(
        theta=alt.Theta(field="Toneladas", type="quantitative"),
        color=alt.Color(field="Categoría", type="nominal"),
        tooltip = ['Categoría', 'Toneladas']
    ).properties(height= 100).configure_view(
        strokeWidth=0
    )
    st.altair_chart(pieAlt, use_container_width=True)
    

st.header(f"Exportaciones por mes del {year}")

line1 = alt.Chart(trad_total_mes).mark_line(color="Orange").encode(
    x = alt.X('Mes', sort=None),
    y = 'Toneladas',
    tooltip = ['Mes', 'Toneladas']
).properties(title = "Exportaciones de productos tradicionales")

st.altair_chart(line1, use_container_width=True)

line2 = alt.Chart(no_trad_total_mes).mark_line(color="Green").encode(
    x = alt.X('Mes', sort=None),
    y = 'Toneladas',
    tooltip = ['Mes', 'Toneladas']
).properties(title = "Exportaciones de productos no tradicionales")

st.altair_chart(line2, use_container_width=True)

st.header(f"Exportaciones por producto del {year}")

valores = set(trad_tipo_mes['Producto'].to_list())
seleccion = st.selectbox('Elija un producto tradicional:',valores)

line3 = alt.Chart(trad_tipo_mes[trad_tipo_mes['Producto'] == seleccion]).mark_line().encode(
    x = alt.X('Mes', sort=None),
    y = 'Toneladas',
    tooltip = ['Mes', 'Toneladas']
).properties(title = f"Exportaciones de {seleccion}")

st.altair_chart(line3, use_container_width=True)

valores2 = set(no_trad_tipo_mes['Producto'].to_list())
seleccion2 = st.selectbox('Elija un producto no  tradicional:',valores2)

line4 = alt.Chart(no_trad_tipo_mes[no_trad_tipo_mes['Producto'] == seleccion2]).mark_line(color="Red").encode(
    x = alt.X('Mes', sort=None),
    y = 'Toneladas',
    tooltip = ['Mes', 'Toneladas']
).properties(title = f"Exportaciones de {seleccion2}")

st.altair_chart(line4, use_container_width=True)
