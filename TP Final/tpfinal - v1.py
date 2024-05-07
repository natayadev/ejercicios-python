import pandas as pd
import numpy as np


# Lectura de todos los archivos de datos (malo si los .csv son pesados)
def lectura_datos(ecommerce_customers_dataset,
                  ecommerce_order_items_dataset,
                  ecommerce_order_payments_dataset,
                  ecommerce_orders_dataset,
                  ecommerce_products_dataset):
    """
    Lee los conjuntos de datos de comercio electrónico y devuelve DataFrames correspondientes.

    Returns:
    - tuple: Una tupla de DataFrames correspondientes a los conjuntos de datos.
    """
    ecommerce_customers_df = pd.read_csv(ecommerce_customers_dataset)
    ecommerce_order_items_df = pd.read_csv(ecommerce_order_items_dataset)
    ecommerce_order_payments_df = pd.read_csv(ecommerce_order_payments_dataset)
    ecommerce_orders_df = pd.read_csv(ecommerce_orders_dataset)
    ecommerce_products_df = pd.read_csv(ecommerce_products_dataset)

    return (ecommerce_customers_df, ecommerce_order_items_df,
            ecommerce_order_payments_df, ecommerce_orders_df,
            ecommerce_products_df)


# Ejemplo de lectura de datos archivo a archivo (recomendado si los .csv son pesados)
"""
def lectura_datos_ecommerce_customers_dataset(ecommerce_customers_dataset):
        ecommerce_customers_df = pd.read_csv(ecommerce_customers_dataset)
        return ecommerce_customers_df

lectura_datos_ecommerce_customers_dataset()
"""

# Exploración de DataFrames
def exploracion_datos(dataframes):
    """
    Imprime información exploratoria sobre los DataFrames proporcionados.
    """

    # Muestra los primeros cinco filas
    print(dataframes[0].head())

    # Muestra la info de nuestro df
    print(dataframes[0].info())

    # Muestra las estadísticas de nuestro df
    print(dataframes[0].describe())

    # Número total de clientes únicos de customers_df
    customers_unique = dataframes[0]["customer_unique_id"].nunique()

    # Promedio de valor de pago por pedido
    promedio = dataframes[2].groupby("order_id")["payment_value"].mean()

    # Determinar la categoría de producto más vendida
    mas_vendidos = dataframes[4].groupby("product_category_name")["product_category_name"].count().idxmax()

    # Calcular el número total de pedidos realizados
    pedidos_realizados = dataframes[3].shape[0]


def establecer_index(dataframes):
    """
    Establecer 'customer_id' como índice para ecommerce_customers_df
    """
    dataframe_commerce = dataframes[0].set_index("customer_id")
    dataframe_producto = dataframes[4].set_index("product_id")


# Elimina los duplicados (sin iterar una lista)
def eliminar_duplicados(dataframes):
    """
        Elimina las filas duplicadas de los DataFrames proporcionados.
    """
    dataframes[0].drop_duplicates() # ecommerce_customers_dataset
    dataframes[1].drop_duplicates() # ecommerce_order_items_dataset
    dataframes[2].drop_duplicates() # ecommerce_order_payments_dataset
    dataframes[3].drop_duplicates() # ecommerce_orders_dataset
    dataframes[4].drop_duplicates() # ecommerce_products_dataset


# Elimina los Not A Number (iterarando los dataframes)
def eliminar_nan(dataframes):
    """
    Elimina filas con valores NaN de los DataFrames proporcionados.
    """

    for dataframe in dataframes:
        dataframe.dropna()


# Rellena los Not A Number (iterarando una lista)
def rellenar_nan(ecommerce_customers_df,
                 ecommerce_order_items_df,
                 ecommerce_order_payments_df,
                 ecommerce_orders_df,
                 ecommerce_products_df):
    """
    Rellena las filas con valores NaN de los DataFrames proporcionados.
    """
    
    lista = [ecommerce_customers_df,
             ecommerce_order_items_df,
             ecommerce_order_payments_df,
             ecommerce_orders_df,
             ecommerce_products_df]

    for dataframe in lista:
        dataframe.fillna(dataframe["columna_a_rellenar"].mean(), inplace=True)


# Elimina las columnas que no necesitamos
def eliminar_columnas_redundantes(dataframe):
    """
    Elimina columnas redundantes de los DataFrames proporcionados.
    """
    lista = ["product_description_lenght","product_photos_qty","product_weight_g","product_length_cm","product_height_cm","product_width_cm","product_name_lenght"]
    dataframe = dataframe.drop(columns=lista)
    print(dataframe)


if __name__ == "__main__":
    # Set de datos
    ecommerce_customers_dataset = 'raw_data/ecommerce_customers_dataset.csv'
    ecommerce_order_items_dataset = 'raw_data/ecommerce_order_items_dataset.csv'
    ecommerce_order_payments_dataset = 'raw_data/ecommerce_order_payments_dataset.csv'
    ecommerce_orders_dataset = 'raw_data/ecommerce_orders_dataset.csv'
    ecommerce_products_dataset = 'raw_data/ecommerce_products_dataset.csv'

    # Ya no llamaremos a las funciones así:
    # lectura_datos()
    # exploracion_datos()
    # eliminar_duplicados()
    # eliminar_nan()

    # Podemos mejorarlo así:
    dataframes = lectura_datos(ecommerce_customers_dataset,
                               ecommerce_order_items_dataset,
                               ecommerce_order_payments_dataset,
                               ecommerce_orders_dataset,
                               ecommerce_products_dataset)
    exploracion_datos(dataframes)
    establecer_index(dataframes)
    #eliminar_duplicados(dataframes)
    #eliminar_nan(dataframes)

    # Eliminación de columnas redundantes, aplica solo a ecommerce_product_df
    eliminar_columnas_redundantes(dataframes[4])
