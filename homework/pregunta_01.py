# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt


def pregunta_01():
    """
    El archivo `files//shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`

    * `Mode_of_Shipment`

    * `Customer_rating`

    * `Weight_in_gms`

    El dashboard generado debe ser similar a este:

    https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

    Para ello, siga las instrucciones dadas en el siguiente video:

    https://youtu.be/AgbWALiAGVo

    Tenga en cuenta los siguientes cambios respecto al video:

    * El archivo de datos se encuentra en la carpeta `data`.

    * Todos los archivos debe ser creados en la carpeta `docs`.

    * Su código debe crear la carpeta `docs` si no existe.

    """

    # Crear carpeta docs si no existe
    if not os.path.exists('docs'):
        os.makedirs('docs')

    # Leer los datos
    df = pd.read_csv('files/input/shipping-data.csv')

    # 1. Gráfico de barras: Shipping per Warehouse
    plt.figure(figsize=(8, 6))
    warehouse_counts = df['Warehouse_block'].value_counts().sort_index()
    plt.bar(warehouse_counts.index, warehouse_counts.values, color='skyblue', edgecolor='black')
    plt.xlabel('Warehouse Block')
    plt.ylabel('Number of Shipments')
    plt.title('Shipping per Warehouse')
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig('docs/shipping_per_warehouse.png')
    plt.close()

    # 2. Gráfico de barras: Mode of Shipment
    plt.figure(figsize=(8, 6))
    mode_counts = df['Mode_of_Shipment'].value_counts()
    plt.bar(mode_counts.index, mode_counts.values, color='lightcoral', edgecolor='black')
    plt.xlabel('Mode of Shipment')
    plt.ylabel('Number of Shipments')
    plt.title('Mode of Shipment')
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig('docs/mode_of_shipment.png')
    plt.close()

    # 3. Gráfico de barras: Average Customer Rating
    plt.figure(figsize=(8, 6))
    rating_avg = df.groupby('Customer_rating')['Customer_rating'].count()
    plt.bar(rating_avg.index, rating_avg.values, color='lightgreen', edgecolor='black')
    plt.xlabel('Customer Rating')
    plt.ylabel('Count')
    plt.title('Average Customer Rating')
    plt.xticks(range(1, 6))
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig('docs/average_customer_rating.png')
    plt.close()

    # 4. Histograma: Weight Distribution
    plt.figure(figsize=(8, 6))
    plt.hist(df['Weight_in_gms'], bins=30, color='plum', edgecolor='black')
    plt.xlabel('Weight (gms)')
    plt.ylabel('Frequency')
    plt.title('Weight Distribution')
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig('docs/weight_distribution.png')
    plt.close()

    # 5. Crear el archivo HTML
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Shipping Dashboard</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #f5f5f5;
        }
        h1 {
            text-align: center;
            color: #333;
        }
        .container {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 20px;
            max-width: 1200px;
            margin: 0 auto;
        }
        .chart {
            background-color: white;
            padding: 15px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .chart img {
            width: 100%;
            height: auto;
            display: block;
        }
    </style>
</head>
<body>
    <h1>Shipping Dashboard</h1>
    <div class="container">
        <div class="chart">
            <img src="shipping_per_warehouse.png" alt="Shipping per Warehouse">
        </div>
        <div class="chart">
            <img src="mode_of_shipment.png" alt="Mode of Shipment">
        </div>
        <div class="chart">
            <img src="average_customer_rating.png" alt="Average Customer Rating">
        </div>
        <div class="chart">
            <img src="weight_distribution.png" alt="Weight Distribution">
        </div>
    </div>
</body>
</html>
"""

    with open('docs/index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)