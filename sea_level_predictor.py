import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Leer datos desde el archivo
    df = pd.read_csv('epa-sea-level.csv')

    # Crear un diagrama de dispersión
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Crear la primera línea de mejor ajuste
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series([i for i in range(1880, 2051)])
    plt.plot(years_extended, intercept + slope * years_extended, 'r', label='Línea de mejor ajuste 1880-2050')

    # Crear la segunda línea de mejor ajuste
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent_extended = pd.Series([i for i in range(2000, 2051)])
    plt.plot(years_recent_extended, intercept_recent + slope_recent * years_recent_extended, 'g', label='Línea de mejor ajuste 2000-2050')

    # Agregar etiquetas y título
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend(loc='upper left')

    # Guardar gráfico y retornar datos para pruebas
    plt.savefig('sea_level_plot.png')
    return plt.gca()