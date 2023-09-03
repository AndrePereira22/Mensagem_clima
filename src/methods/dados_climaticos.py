import requests
import json

def pegar_clima(cidade):
   URL_CLIMA = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid=63fdd93d9a13e20018e653478a84cab3&lang=pt_br&units=metric"
   resp = requests.get(URL_CLIMA)
   return json.loads(resp.content.decode('utf8')) if resp.status_code == 200 else None