import pandas as pd

def Salvar_csv(df):
    df.to_csv('dados_carregamento.csv' , encoding='utf-8-sig')