import pandas as pd
import time

from src.methods.formato_dados import formatar
from src.methods.criacao_Mensagem import generate_ai_menssage
from src.methods.salvar_csv import Salvar_csv

#pip install -r requirements.txt

# Lendo o arquivo  Excell
df = pd.read_excel("dados_extracao.xlsx")


# Lista para salvar nosso dicionario personalizado
dados= []
#Lista para salvar as mensagens criados pelo Chat GPT
mensagens = []

for i, infos in df.iterrows():
  info = formatar( infos['Nome'],  infos['Cidade'])
  dados.append(info)

for temp in dados:
    mensagens.append(generate_ai_menssage(temp))

# Adicionando coluna com as mensagens ao DataFrame
df['mensagem_clima'] =mensagens

# Salvar dados em CSV
Salvar_csv(df)
