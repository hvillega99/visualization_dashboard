import streamlit as st
import pandas as pd

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

st.text('Productos no tradicionales')
st.bar_chart(noTradicionales['Toneladas'])
