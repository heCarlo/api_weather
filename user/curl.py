import requests

url = 'http://localhost:8000/api/token/'
headers = {'Content-Type': 'application/json'}
data = {'username': 'davidattenborough', 'password': 'boatymcboatface'}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    print('Token de acesso:', response.json()['access'])
    print('Token de atualização:', response.json()['refresh'])
else:
    print('Erro:', response.status_code)
