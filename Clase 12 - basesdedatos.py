from sqlalchemy import create_engine

# Cadena de conexión
DB_USERNAME = 'username'
DB_PASSWORD = 'password'
DB_HOSTNAME = 'hostname'
DB_DATABASE = 'database'

connection_string = f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOSTNAME}/{DB_DATABASE}'

# Crear el motor de SQLAlchemy
engine = create_engine(connection_string)

# Prueba de la conexión
try:
    with engine.connect() as connection:
        print("¡Conexión exitosa a la base de datos!")
except Exception as e:
    print("Error al conectar a la base de datos:", e)

#query = """SELECT * FROM table_name"""

