import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Descargar los datos desde la API
url = "https://api.covidtracking.com/v1/us/daily.json"
response = requests.get(url)

# 2. Convertir la respuesta en un DataFrame de pandas
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

# 3. Convertir la columna 'date' en un formato de fecha
df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')

# 4. Mostrar la estructura del DataFrame
print(df.info())

# 5. Resumen estadístico de las columnas numéricas
print(df.describe())

# 6. Visualización de algunas tendencias temporales
# Ordenar los datos por fecha
df = df.sort_values(by='date')

# Graficar casos positivos y muertes en el tiempo
plt.figure(figsize=(14, 7))

plt.subplot(2, 1, 1)
plt.plot(df['date'], df['positiveIncrease'], label='New Positive Cases', color='blue')
plt.title('Daily New Positive Cases in the US')
plt.ylabel('Number of Cases')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(df['date'], df['deathIncrease'], label='New Deaths', color='red')
plt.title('Daily New Deaths in the US')
plt.ylabel('Number of Deaths')
plt.xlabel('Date')
plt.legend()

plt.tight_layout()
plt.show()

# 7. Correlación entre las variables

# Convertir la columna 'dateChecked' en un formato de fecha
df['dateChecked'] = pd.to_datetime(df['dateChecked'], errors='coerce')

# Eliminar filas con fechas no válidas (opcional)
df = df.dropna(subset=['dateChecked'])

# Ver los primeros registros para confirmar la operación
print(df[['dateChecked']].head())

corr_matrix = df.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# 8. Análisis de tendencias
# Media móvil de nuevos casos y muertes
df['7_day_avg_positive'] = df['positiveIncrease'].rolling(window=7).mean()
df['7_day_avg_deaths'] = df['deathIncrease'].rolling(window=7).mean()

plt.figure(figsize=(14, 7))

plt.subplot(2, 1, 1)
plt.plot(df['date'], df['7_day_avg_positive'], label='7-Day Average New Positive Cases', color='blue')
plt.title('7-Day Average of New Positive Cases')
plt.ylabel('Number of Cases')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(df['date'], df['7_day_avg_deaths'], label='7-Day Average New Deaths', color='red')
plt.title('7-Day Average of New Deaths')
plt.ylabel('Number of Deaths')
plt.xlabel('Date')
plt.legend()

plt.tight_layout()
plt.show()

