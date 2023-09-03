import openai



def generate_ai_menssage(dados) :
  
  API_KEY = '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'
  openai.api_key = API_KEY
  completion = openai.ChatCompletion.create(
      model ="gpt-3.5-turbo",
      messages = [
          {"role": "system", "content":"Você é um especialista em meteorologia."},
          {"role": "user", "content": f"crie um alerta metereologico para {dados['nome']} passandoos seguintes dados {dados['cidade']}, {dados['nuvens']}, {dados['temperatura']} °C, {dados['humidade']}%, {dados['vento']} m/s (máximo 200 caracteres)"}
      ]
  )
  return  completion.choices[0].message.content # strip("'")