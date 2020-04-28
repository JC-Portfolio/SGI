import os
from os import environ
import pprint 

# PARA DEFINIR UMA VARIAVEL DE AMBIENTE utilizamos a seguinte notação

# os.environ['NOME_X'] = "valor da var"

#Podemos utilizar o seguinte esquema para manipular variaveis que talvez não existam
# print("MY_HOME:", os.environ.get('MY_HOME', "Environment variable does not exist"))
#Dessa forma não será levantada nenhuma exceção


# print("User's Environment variable:")
# pprint.pprint(dict(env_var), width = 1)


APP_NAME = environ.get('APP_NAME', "SGI")
APP_HOST = environ.get("APP_HOST", "127.0.0.1")
APP_PORT = environ.get("APP_PORT", "8000")
APP_ENV = environ.get('APP_ENV', 'local')
APP_KEY = environ.get('APP_KEY', '309a3a45-0e44-4906-b629-bb61269c927f')
APP_DEBUG = False if APP_ENV == 'prod' else True


DB_USER = environ.get('DB_USER', 'postgres')
DB_PASSWORD = environ.get('DB_PASSWORD', '123456')
DB_HOST = environ.get('DB_HOST', '127.0.0.1')
DB_PORT = environ.get('DB_PORT', 5432)
DB_NAME = environ.get('DB_NAME', 'sgi')


DATABASE_URI = f"postgres://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"