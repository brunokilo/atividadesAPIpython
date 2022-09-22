import requests
import json
r = requests.get("https://api.hgbrasil.com/finance?key=6e7ee483")
moeda = json.loads(r.text)

dolar = moeda['results']['currencies']['USD']['buy']
euro = moeda['results']['currencies']['EUR']['buy']

real=float(input('Insira o valor em reais:'))

print('###################################')
print('#####      COTAÇÕES          ######')
print('##### Dolar (USD) é:', real*dolar,'######')
print('##### EURO (EUR) é:', real*euro,'  ######')
print('###################################')