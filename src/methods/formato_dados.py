from src.methods.dados_climaticos import *


def formatar(nome, cidade):

  clima = pegar_clima(cidade)

  nuvens = clima['weather'][0]['description']
  temperatura = clima['main']['temp']
  humidade = clima['main']['humidity'] 
  vento = clima['wind']['speed'] 

  return  {"nome":{nome},"nuvens":f"{nuvens}", "temperatura":f"{temperatura}",
         "humidade":f"{humidade}","vento":f"{vento}","cidade":f"{cidade}"}