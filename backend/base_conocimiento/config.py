from dotenv import load_dotenv
import os

load_dotenv()

# Cargar las variables de entorno
pwd = os.getenv('DB_PASSWORD')
user = os.getenv('DB_USER')
host = os.getenv('DB_HOST')
db = os.getenv('DB_NAME')
server = os.getenv('SERVER')

# Crear la cadena de conexión
DATABASE_CONNECTION = f'{server}://{user}:{pwd}@{host}/{db}'