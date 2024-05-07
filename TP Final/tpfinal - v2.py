import pandas as pd
import matplotlib.pyplot as plt


def lectura_datos_ecommerce_customers_dataset(dataset):
    """
    Lee el conjunto de datos de ecommerce_customers y devuelve el DataFrame correspondiente.
    """
    ecommerce_customers_df = pd.read_csv(dataset)
    return ecommerce_customers_df


def lectura_datos_ecommerce_order_items_dataset(dataset):
    """
    Lee el conjunto de datos de ecommerce_order_items y devuelve el DataFrame correspondiente.
    """
    ecommerce_order_items_df = pd.read_csv(dataset)
    return ecommerce_order_items_df


def lectura_datos_ecommerce_order_payments_dataset(dataset):
    """
    Lee el conjunto de datos de ecommerce_order_payments y devuelve el DataFrame correspondiente.
    """
    ecommerce_order_payments_df = pd.read_csv(dataset)
    return ecommerce_order_payments_df


def lectura_datos_ecommerce_orders_dataset(dataset):
    """
    Lee el conjunto de datos de ecommerce_orders y devuelve el DataFrame correspondiente.
    """
    ecommerce_orders_df = pd.read_csv(dataset)
    return ecommerce_orders_df


def lectura_datos_ecommerce_products_dataset(dataset):
    """
    Lee el conjunto de datos de ecommerce_products y devuelve el DataFrame correspondiente.
    """
    ecommerce_products_df = pd.read_csv(dataset)
    return ecommerce_products_df


def establecer_index(dataframes):
    """
    Establecer los id como índice para los DataFrames proporcionados.
    """
    dataframes[0] = dataframes[0].set_index("customer_id")
    dataframes[1] = dataframes[1].set_index("order_item_id")
    dataframes[2] = dataframes[2].set_index("order_id")
    dataframes[3] = dataframes[3].set_index("order_id")
    dataframes[4] = dataframes[4].set_index("product_id")


def eliminar_duplicados(dataframes):
    """
        Elimina las filas duplicadas de los DataFrames proporcionados.
    """

    for i, dataframe in enumerate(dataframes):
        dataframes[i] = dataframe.drop_duplicates()


def eliminar_nan(dataframes):
    """
    Elimina filas con valores NaN de los DataFrames proporcionados.
    """

    for i, dataframe in enumerate(dataframes):
        dataframes[i] = dataframe.dropna()


def eliminar_columnas_redundantes(dataframes):
    """
    Elimina columnas redundantes de los DataFrames proporcionados.
    """

    columnas_ecommerce_customers = []
    dataframes[0] = dataframes[0].drop(columns=columnas_ecommerce_customers)

    columnas_ecommerce_order_items = ["order_id", "product_id"]
    dataframes[1] = dataframes[1].drop(columns=columnas_ecommerce_order_items)

    columnas_ecommerce_order_payments = []
    dataframes[2] = dataframes[2].drop(
        columns=columnas_ecommerce_order_payments)

    columnas_ecommerce_orders = []
    dataframes[3] = dataframes[3].drop(columns=columnas_ecommerce_orders)

    columnas_ecommerce_products = ["product_description_lenght", "product_photos_qty", "product_weight_g",
                                   "product_length_cm", "product_height_cm", "product_width_cm", "product_name_lenght"]
    dataframes[4] = dataframes[4].drop(columns=columnas_ecommerce_products)


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
    clientes_unicos = dataframes[0]["customer_unique_id"].nunique()

    # Promedio de valor de pago por pedido
    promedio = dataframes[2].groupby("order_id")["payment_value"].mean()

    # Calcular el número total de pedidos realizados
    pedidos_realizados = dataframes[3].shape[0]

    # Determinar la categoría de producto más vendida
    mas_vendidos = dataframes[4].groupby("product_category_name")[
        "product_category_name"].count().idxmax()

    # Crea un dataframe con los datos anteriores
    df_exploracion = pd.DataFrame({
        "clientes_unicos": [clientes_unicos],
        "promedio_pago_por_pedido": [promedio.mean()],
        "categoria_mas_vendida": [mas_vendidos],
        "pedidos_realizados": [pedidos_realizados]
    })

    return df_exploracion

def exportar_excel(dataframes):
    #dataframes[0].to_excel("prueba.xlsx", index=False)

    file = "dataframes.xlsx"
    with pd.ExcelWriter(file) as writer:
        dataframes[0].to_excel(writer, sheet_name="customers", index=False)
        dataframes[1].to_excel(writer, sheet_name="order_items", index=False)
        dataframes[2].to_excel(writer, sheet_name="order_payments", index=False)
        dataframes[3].to_excel(writer, sheet_name="orders", index=False)
        dataframes[4].to_excel(writer, sheet_name="products", index=False)
        dataframes[5].to_excel(writer, sheet_name="attached", index=False)


if __name__ == "__main__":
    # Set de datos
    ecommerce_customers_dataset = 'raw_data/ecommerce_customers_dataset.csv'
    ecommerce_order_items_dataset = 'raw_data/ecommerce_order_items_dataset.csv'
    ecommerce_order_payments_dataset = 'raw_data/ecommerce_order_payments_dataset.csv'
    ecommerce_orders_dataset = 'raw_data/ecommerce_orders_dataset.csv'
    ecommerce_products_dataset = 'raw_data/ecommerce_products_dataset.csv'

    dataframes = [
        lectura_datos_ecommerce_customers_dataset(ecommerce_customers_dataset),
        lectura_datos_ecommerce_order_items_dataset(
            ecommerce_order_items_dataset),
        lectura_datos_ecommerce_order_payments_dataset(
            ecommerce_order_payments_dataset),
        lectura_datos_ecommerce_orders_dataset(ecommerce_orders_dataset),
        lectura_datos_ecommerce_products_dataset(ecommerce_products_dataset)
    ]

    establecer_index(dataframes)
    eliminar_duplicados(dataframes)
    eliminar_nan(dataframes)
    eliminar_columnas_redundantes(dataframes)

    df_exploracion = exploracion_datos(dataframes)
    dataframes.append(df_exploracion)
    print(dataframes)
    
    exportar_excel(dataframes)

    # Graficar con matplotlib y pandas
    dataframes[4]["product_category_name"].value_counts().plot(kind="bar")
    plt.title("Gráfico de barras de producto")
    plt.savefig("productos_bar.png")

    dataframes[4]["product_category_name"].value_counts().plot(kind="pie")
    plt.title("Gráfico de torta de producto")
    plt.savefig("productos_pie.png")