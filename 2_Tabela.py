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

empresa = st.sidebar.selectbox(
    'Qual empresa?',
    ('NAGEM', 'IBYTE', 'HAPVIDA'))

lista_estados = ["AL","AM","AP","BA","CE","DF","ES","GO","MA","MG","MS","MT","PA","PB","PE","PI","PR","RJ","RN","RR","RS","SC","SE","SP","TO"]

estado = st.sidebar.selectbox(
    'Qual Estado?',lista_estados)
st.sidebar.divider()
#st.write(nag)
st.write("Total de Reclamações por Empresa:")
col1, col2, col3 = st.columns(3)
col1.metric("Nagem", (df[df.EMPRESA == "NAGEM"])["ID"].count(), "33,16%")
col2.metric("Ibyte", (df[df.EMPRESA == "IBYTE"])["ID"].count(), "33,16%")
col3.metric("Hapvida", (df[df.EMPRESA == "HAPVIDA"])["ID"].count(), "33,68%")
st.divider()
st.write(df[(df.EMPRESA == empresa) & (df.ESTADO == estado)].head(qtd),weith=200)

#st.write(df[df['ESTADO'] == estado])

#st.line_chart((df[df['ESTADO'] == estado and df['EMPRESA'] == empresa]).groupby('MES').nunique()['ID'])
st.divider()
st.metric(label="Total de Reclamações no Estado de " + estado + ", da empresa " + empresa, value=(df[(df.EMPRESA == empresa) & (df.ESTADO == estado)])["ID"].count())
df1 = df[(df.EMPRESA == empresa) & (df.ESTADO == estado)]
st.write(df1["STATUS"].value_counts())
st.divider()
st.subheader("Evolução temporal do Número de Reclamações do Estado de " + estado)
st.line_chart(df1.groupby('TEMPO').nunique()['ID'])
