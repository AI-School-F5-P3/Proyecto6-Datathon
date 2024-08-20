import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Descargar los datos desde la API
url = "https://api.covidtracking.com/v1/states/current.json"
response = requests.get(url)

# Convertir la respuesta en un DataFrame de pandas
if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
else:
    print(f"Error en la solicitud: {response.status_code}")


# Verificar cuántos datos nulos, vacíos o en cero hay en cada columna
null_counts = df.isnull().sum()  # Contar los valores nulos
zero_counts = (df == 0).sum()    # Contar los valores que son cero

# Combinar las dos series en un DataFrame para mostrar los resultados
null_and_zero_counts = pd.DataFrame({
    'Null Counts': null_counts,
    'Zero Counts': zero_counts
})

print(null_and_zero_counts)

# Convertir la columna 'date' en un formato de fecha
df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')

# Mostrar la estructura del DataFrame
print(df.info())

# Resumen estadístico de las columnas numéricas
print(df.describe())

# Ordenar los datos por fecha
df = df.sort_values(by='date')

# Gráficos de Dispersión (Scatter Plots)

"""Los gráficos de dispersión son útiles para visualizar la relación entre dos variables numéricas. Cada punto en el gráfico representa un par de valores (x, y) de las dos variables.
"""
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Datos de ejemplo
df = pd.DataFrame(data)

# Ajustar el tamaño del gráfico para dar más espacio a las etiquetas
plt.figure(figsize=(12, 6))

# Obtener las posiciones actuales de las etiquetas y crear un nuevo espaciado
positions = np.arange(len(df['state'].unique()))
plt.xticks(positions, df['state'].unique(), rotation=0, ha='center')  # Sin rotación (horizontal), y centradas

# Añadir márgenes para que las etiquetas no se apiñen
plt.subplots_adjust(right=2)

# Gráfico de dispersión simple
sns.scatterplot(x='state', y='positive', data=df)
plt.xlabel('States')
plt.ylabel('Positives')
plt.title('Gráfico de Dispersión')
plt.show()

