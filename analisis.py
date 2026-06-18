# ANÁLISIS DE VENTAS - EQUIPO A
import pandas as pd
import numpy as np

datos = {
    'mes': ['Ene', 'Feb', 'Mar', 'Abr', 'May'],
    'ventas': [1200, 1500, 1100, 1800, 2100]
}

df = pd.DataFrame(datos)
print(df)
print(f"\nPromedio de ventas: {df['ventas'].mean()}")
print(f"Mes con más ventas: {df.loc[df['ventas'].idxmax(), 'mes']}")
