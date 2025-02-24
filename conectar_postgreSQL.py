# install psycopg2-binary
import psycopg2
import os
from dotenv import load_dotenv
load_dotenv('.env')
#MY_CONNECTION = os.getenv("POSTGRES_PRISMA_URL")
#MY_CONNECTION = os.environ.get('POSTGRES_PRISMA_URL')
#my_prueba = os.getenv("PRUEBA_5")
my_prueba =  os.getenv("PRUEBA_5")

# URL de conexión desde las variables de entorno
#DATABASE_URL = os.getenv("DATABASE_URL", "postgres://usuario:password@host:puerto/dbname")

try:
    # Establecer conexión
    #conn = psycopg2.connect(MY_CONNECTION, sslmode="require")


    # Crear un cursor
    #cursor = conn.cursor()

    # Ejecutar una consulta
    #cursor.execute("SELECT NOW();")
    #result = cursor.fetchone()

    #print("Conexión exitosa. Fecha y hora del servidor:", result[0])

    # Cerrar conexión
    #cursor.close()
    #conn.close()

#except:
#    print("Error conectando a la base de datos:")


#####
#try:
#    #connection = psycopg2.connect(f"postgresql://{pas_sql.user_sql}:{pas_sql.password_sql}@alpha.europe.mkdb.sh:5432/{pas_sql.name_sql}")
#    connection = psycopg2.connect(f"postgresql://ukanzjez:wcnekxjkudklpgwqcmdk@alpha.europe.mkdb.sh:5432/rnpnasxv") 
    conn = psycopg2.connect(my_prueba)
    cursor = conn.cursor()
except: 
      print("No se ha podido conectar a la base de datos.")
      
# insertar datos
def insertar_sql(eje):
    cursor.execute(eje)
    #connection.commit()
    conn.commit()
    
# recuperar un único registro
def sql_select_one(table, where):
    cursor.execute(f"SELECT * FROM {table} WHERE {where}")
    for pay in cursor:
        return pay[2]

# recuperar todos los datos de una tabla
def sql_select_all(table, order="DESC"):
    cursor.execute(f"SELECT * FROM {table} ORDER BY id {order}")
    return cursor

# borrar datos de la tabla
insertar_sql("TRUNCATE TABLE precios")
# crear tabla de precios si no existe 
insertar_sql(f"CREATE TABLE IF NOT EXISTS precios(id SERIAL PRIMARY KEY,estado CHAR(20) NOT NULL,precio FLOAT)")
# crear tabla de trayectos si no existe 
insertar_sql('''CREATE TABLE IF NOT EXISTS trayecto(id SERIAL PRIMARY KEY, fecha TIMESTAMP NOT NULL DEFAULT NOW(), precio DECIMAL(10,2) NOT NULL)''')
# crear tabla de usuarios si no existe 
insertar_sql('''CREATE TABLE IF NOT EXISTS usuarios (id SERIAL PRIMARY KEY, nombre VARCHAR(100) NOT NULL, usuario VARCHAR(50) UNIQUE NOT NULL)''')

#insertar_sql('''INSERT INTO usuarios(nombre, usuario) VALUES('Juan', 'a94652aa97c7211ba8954dd15a3cf838')''')
insertar_sql('''INSERT INTO precios(estado, precio) VALUES('parado', 3.02)''')
insertar_sql('''INSERT INTO precios(estado, precio) VALUES('marcha', 0.05)''')