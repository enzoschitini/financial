import streamlit as st
import pandas as pd
from pandas_datareader import data as web

from plotly.graph_objs import Layout
import plotly.graph_objects as go

from utils.pages import PagesLive
from utils.guida import GuidaDataframe
from utils.analise import Analise
from utils.graficos import FinancialPlots

"""
requirements.txt

streamlit==1.24.0
pandas==2.0.3
pandas-datareader==0.10.0
plotly==5.15.0
yfinance==0.2.30
itertools==0.1
time==3.9.6
"""

st.set_page_config(layout='wide', page_title='Financial shares of large companies',
                   page_icon="img\Icone.png")
pl = PagesLive

st.sidebar.image("img\Investment 1.png")
st.sidebar.write('# Financial shares of large companies')
st.sidebar.write('Filtro do dataset - Escolha como quer ver os dados:')

resposta = st.sidebar.selectbox(f"Escolha uma empresa:", ['Petrobras', 'Coca-Cola', 'Amazon', 'Tesla', 'Itaú Unibanco', 'Emirates'])
st.write(f"Você escolheu:")
st.write(f'## {resposta}')

if resposta == 'Petrobras':
    df = pl.dataframe_ativo('PBR', resposta)
    df = pl.engenharia_de_atributos(df)

    pl = Analise
    pl.painel_geral(df, 'Petróleo Brasileiro S.A. - Petrobras (PBR)', "img\Petrobras.png")

elif resposta == 'Coca-Cola':
    df = pl.dataframe_ativo('KO', resposta)
    #st.write(df)
    df = pl.engenharia_de_atributos(df)

    pl = Analise
    pl.painel_geral(df, 'The Coca-Cola Company (KO)', "img\Coca-Cola.png")

elif resposta == 'Amazon':
    df = pl.dataframe_ativo('AMZN', resposta)
    df = pl.engenharia_de_atributos(df)

    pl = Analise
    pl.painel_geral(df, 'Amazon - Stock market shares', "img\Amazon.png")

elif resposta == 'Tesla':
    df = pl.dataframe_ativo('TSLA', resposta)
    df = pl.engenharia_de_atributos(df)

    pl = Analise
    pl.painel_geral(df, 'Tesla, Inc. (TSLA)', "img\Tesla.png")

elif resposta == 'Itaú Unibanco':
    df = pl.dataframe_ativo('ITUB', resposta)
    df = pl.engenharia_de_atributos(df)

    pl = Analise
    pl.painel_geral(df, 'Itaú Unibanco Holding S.A. (ITUB)', "img\Itaú.png")

elif resposta == 'Emirates':
    df = pl.dataframe_ativo('0P0001LIHZ', resposta)
    df = pl.engenharia_de_atributos(df)

    pl = Analise
    pl.painel_geral(df, 'Emirates Global Sukuk S USD Acc', "img\Emirates.png")