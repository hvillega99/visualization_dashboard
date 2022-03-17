import streamlit as st
import pandas as pd
import altair as alt


st.title('Exportaciones no petroleras de Ecuador a Estados Unidos')

file = 'exportaciones.csv'
df = pd.read_csv(file)

year = st.slider('Año', min_value=2001, max_value=2021, value=2001, step=1)

noPetroleros = df[ df['No Petrolero/Petrolero'] == 'No Petrolero'   ]
noPetrolerosByYear = noPetroleros[ noPetroleros['Año'] == year ]

noTradicional_index = noPetrolerosByYear['Tradicional/No tradicional'] == 'NO TRADICIONAL'
tradicional_index = noPetrolerosByYear['Tradicional/No tradicional'] == 'TRADICIONAL'

tradicionales = noPetrolerosByYear[tradicional_index].groupby('Producto Principal (Nivel 4)').sum()
noTradicionales = noPetrolerosByYear[noTradicional_index].groupby('Producto Principal (Nivel 4)').sum()


st.text('Productos tradicionales')
st.bar_chart(tradicionales['Toneladas'])

st.text('Productos no tradicionales - normal')
st.bar_chart(noTradicionales['Toneladas'])


st.text('Productos no tradicionales - seleccion')
valores=list(noTradicionales.index.values)
options = st.multiselect(
     'What are your favorite colors',
     valores,
     ['Arroz', 'Bebidas'])

st.write('You selected:', options)
st.bar_chart(noTradicionales['Toneladas'][options])




#st.text('Productos no tradicionales-Vertical')
#data = pd.melt(noTradicionales['Toneladas'].reset_index(), id_vars=["Producto Principal (Nivel 4)"])
#chart = (
#    alt.Chart(data)
#    .mark_bar()
#    .encode(
#        x=alt.X("value", type="quantitative", title=""),
#        y=alt.Y("Producto Principal (Nivel 4)", type="nominal", title=""),
#        color=alt.Color("variable", type="nominal", title=""),
#        order=alt.Order("variable", sort="descending"),
#    )
#)
#st.altair_chart(chart, use_container_width=True)

