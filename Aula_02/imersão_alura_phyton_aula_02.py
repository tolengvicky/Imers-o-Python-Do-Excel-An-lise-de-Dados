# -*- coding: utf-8 -*-
"""Imersão Alura Phyton - Aula 02

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YMnQXOPC61Et-QF5qoEHZg7VmkzvqEdq

Aula 02 - Importação
"""

import pandas as pd

df_principal = pd.read_excel("/Imersão Python - Tabela de ações_Aula02.xlsx",sheet_name="Principal")
df_principal

df_total_de_acoes = pd.read_excel("/Imersão Python - Tabela de ações_Aula02.xlsx",sheet_name="Total_de_acoes")
df_total_de_acoes

df_ticker = pd.read_excel("/Imersão Python - Tabela de ações_Aula02.xlsx",sheet_name="Ticker")
df_ticker

df_chatgpt = pd.read_excel("/Imersão Python - Tabela de ações_Aula02.xlsx",sheet_name="Chatgpt")
df_chatgpt