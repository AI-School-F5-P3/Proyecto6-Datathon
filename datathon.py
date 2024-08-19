import requests

# Definir la URL del endpoint al que quieres conectarte
url = "https://api.covidtracking.com/v1/us/daily.json"  # Ejemplo para obtener datos diarios de EE.UU.

# Hacer la solicitud GET
response = requests.get(url)

# Comprobar si la solicitud fue exitosa (código 200)
if response.status_code == 200:
    # Convertir la respuesta en JSON
    data = response.json()
    
    # Mostrar la data (o hacer lo que necesites con ella)
    print(data)
else:
    print(f"Error en la solicitud: {response.status_code}")