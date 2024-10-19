import pandas as pd
from sqlalchemy import create_engine
#install pymysql
# Conectar a la base de datos MySQL
usuario = 'root'
contraseña = 'root123'
host = 'localhost'
base_datos = 'iowa_tmp'

# Crear la conexión a MySQL usando SQLAlchemy
engine = create_engine(f'mysql+pymysql://{usuario}:{contraseña}@{host}/{base_datos}')

# Leer el CSV en bloques (chunks)
ruta_csv = 'iowa-liquor.csv'
chunk_size = 10000  # Tamaño del bloque (número de filas)

# Iterar sobre los bloques y cargar en MySQL
i=1
for chunk in pd.read_csv(ruta_csv, chunksize=chunk_size):
    if i>100: #solo vamos a subir hasta 1 millon de registros
        break
    chunk.to_sql(name='tmp_iowa_liquor', con=engine, if_exists='append', index=False)
    print(f'{i}.- Se cargó un bloque de {chunk_size} filas.')
    i+=1

print("Importación completada.")
