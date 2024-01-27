#pip install pandas
#pip install numpy
#pip install plotly.express
#pip install panel
#pip install jupyter_bokeh
#pip install ipywidgets
#pip install streamlit

import pandas as pd
import numpy as np
import matplotlib as mp
import streamlit as st

st.title("Número de Reclamações")
st.subheader("Empresas: HAPVIDA, NAGEM e IBYTE")
st.subheader("Aluno: Antonio Davi Silva Nobre")
st.divider()
df_HAP = pd.read_csv('RECLAMEAQUI_HAPVIDA.csv')
df_IBY = pd.read_csv('RECLAMEAQUI_IBYTE.csv')
df_NAG = pd.read_csv('RECLAMEAQUI_NAGEM.csv')

df_HAP['EMPRESA'] = "HAPVIDA"
df_NAG['EMPRESA'] = "NAGEM"
df_IBY['EMPRESA'] = "IBYTE"


df = pd.concat([df_HAP, df_NAG,df_IBY]).reset_index()

df.drop('index',axis=1,inplace=True)
df['TEMPO']=pd.to_datetime(df['TEMPO'])
df['ESTADO'] = [x.split(' - ')[1] for x in df['LOCAL']]

st.sidebar.subheader("Menu de Filtros")
st.sidebar.divider()
qtd = st.sidebar.slider('Quantas reclamações você deseja filtrar?', 0, 1000, 500)
st.sidebar.divider()

empresa = st.sidebar.selectbox(
    'Qual empresa?',
    ('NAGEM', 'IBYTE', 'HAPVIDA'))

lista_estados = ["AL","AM","AP","BA","CE","DF","ES","GO","MA","MG","MS","MT","PA","PB","PE","PI","PR","RJ","RN","RR","RS","SC","SE","SP","TO"]

estado = st.sidebar.selectbox(
    'Qual Estado?',lista_estados)

#st.write(nag)
st.write(df[(df.EMPRESA == empresa) & (df.ESTADO == estado)].head(qtd))

#st.write(df[df['ESTADO'] == estado])

#st.line_chart((df[df['ESTADO'] == estado and df['EMPRESA'] == empresa]).groupby('MES').nunique()['ID'])
st.metric(label="Total de Reclamações no Estado de "+option2, value=(df[df['ESTADO'] == estado])["ID"].count())
df1 = df[df['ESTADO'] == estado]
st.write(df1["STATUS"].value_counts())

st.subheader("Evolução temporal do Número de Reclamações do Estado de "+estado)
st.line_chart(df1.groupby('MES').nunique()['ID'])
