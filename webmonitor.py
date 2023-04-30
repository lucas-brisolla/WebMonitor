import requests 

r = requests.get('https://github.com/lucas-brisolla')

if r.content != r.content:
    print("mudou")
else:
    print("continua igual")