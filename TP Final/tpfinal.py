import pandas as pd

ecommerce_customers_dataset = 'raw_data/ecommerce_customers_dataset.csv'
ecommerce_order_items_dataset = 'raw_data/ecommerce_order_items_dataset.csv'
ecommerce_order_payments_dataset = 'raw_data/ecommerce_order_payments_dataset.csv'
ecommerce_orders_dataset = 'raw_data/ecommerce_orders_dataset.csv'
ecommerce_products_dataset = 'raw_data/ecommerce_products_dataset.csv'


def lectura_datos(ecommerce_customers_dataset,
                  ecommerce_order_items_dataset,
                  ecommerce_order_payments_dataset,
                  ecommerce_orders_dataset,
                  ecommerce_products_dataset):
    """ snaskjndjksk """

    ecommerce_customers_df = pd.read_csv(ecommerce_customers_dataset)
    ecommerce_order_items_df = pd.read_csv(ecommerce_order_items_dataset)
    ecommerce_order_payments_df = pd.read_csv(ecommerce_order_payments_dataset)
    ecommerce_orders_df = pd.read_csv(ecommerce_orders_dataset)
    ecommerce_products_df = pd.read_csv(ecommerce_products_dataset)

def lectura_datos_ecommerce_customers_dataset(ecommerce_customers_dataset):
    ecommerce_customers_df = pd.read_csv(ecommerce_customers_dataset)
    return ecommerce_customers_df

lectura_datos_ecommerce_customers_dataset()

def exploracion_datos(ecommerce_customers_df,
                      ecommerce_order_items_df,
                      ecommerce_order_payments_df,
                      ecommerce_orders_df,
                      ecommerce_products_df):
    # Muestra los primeros diez filas
    print(ecommerce_customers_df.head())

    # Muestra la info de nuestro df
    print(ecommerce_customers_df.info())

    print(ecommerce_customers_df.describe())


def eliminar_duplicados(ecommerce_customers_df,
                        ecommerce_order_items_df,
                        ecommerce_order_payments_df,
                        ecommerce_orders_df,
                        ecommerce_products_df):

    ecommerce_customers_df = ecommerce_customers_df.drop_duplicates()
    ecommerce_order_payments_df = ecommerce_order_payments_df.drop_duplicates()
    ecommerce_order_items_df = ecommerce_order_items_df.drop_duplicates()
    ecommerce_orders_df = ecommerce_orders_df.drop_duplicates()
    ecommerce_products_df = ecommerce_products_df.drop_duplicates()


def eliminar_nan(ecommerce_customers_df,
                 ecommerce_order_items_df,
                 ecommerce_order_payments_df,
                 ecommerce_orders_df,
                 ecommerce_products_df):

    lista = [ecommerce_customers_df,
             ecommerce_order_items_df,
             ecommerce_order_payments_df,
             ecommerce_orders_df,
             ecommerce_products_df]

    for df in lista:
        df.dropnan()


def rellenar_nan():
    pass


def eliminar_colummnas_redundantes():
    lista = ["product_category_name", "product_name_lenght"]
    ecommerce_customers_df = ecommerce_customers_df.drop(columns=lista)
    print(ecommerce_customers_df)


lectura_datos()
eliminar_duplicados()
eliminar_nan()
eliminar_colummnas_redundantes()
