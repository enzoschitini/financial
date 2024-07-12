import streamlit as st
import pandas as pd
from pandas_datareader import data as web

from plotly.graph_objs import Layout
import plotly.graph_objects as go

from pages import PagesLive
from guida import GuidaDataframe
from analise import Analise
from graficos import FinancialPlots

st.set_page_config(layout='wide', page_title='Financial shares of large companies')
pl = PagesLive

#st.sidebar.image("img\Investment 1.png")
st.sidebar.write('# Financial shares of large companies')
st.sidebar.write('Filtro do dataset - Escolha como quer ver os dados:')

resposta = st.sidebar.selectbox(f"Escolha uma empresa:", ['Home', 'Petrobras', 'Coca-Cola', 'Amazon', 'Tesla', 'Itaú Unibanco', 'Emirates'])
st.write(f"Você escolheu:")
st.write(f'## {resposta}')

if resposta == 'Petrobras':
    df = pd.read_csv('Petróleo Brasileiro S.A. - Petrobras (PBR).csv')
    #df = pl.dataframe_ativo('PBR', resposta)
    #df = pl.engenharia_de_atributos(df)

    pl = Analise
    pl.painel_geral(df, 'Petróleo Brasileiro S.A. - Petrobras (PBR)', "img\Petrobras.png")