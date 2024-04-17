import requests
response=requests.get(url='http://api.open-notify.org/iss-now.json')
print(response)
print(response.status_code)
response.raise_for_status()
data=response.json()
print(data)
latitude=data['iss_position']['latitude']
longitude=data['iss_position']['longitude']
coordinates=(latitude,longitude)
print(coordinates)