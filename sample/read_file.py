import requests

params = (
('op', 'CREATE')
)
file = open('./assets/images.jpg','rb')

response =  requests.put('http://localhost:9000/input',params=params,files=file)
print(response.status_code)