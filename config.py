import os
import psycopg2

SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))
# Enable debug mode.
DEBUG = True

SQLALCHEMY_DATABASE_URI = "host = 'ec2-3-231-69-204.compute-1.amazonaws.com', port = 5432, database = 'd3hr8qndm4p50h', user = 'oxwttxarfidlxi', password = '89e47cacfc5926776ab52a7e485b08a91bf9632736ca0843d80b6356b506f3f2'"
SQLALCHEMY_TRACK_MODIFICATIONS = False


CARPETA = os.path.join('uploads')
CARPETA_PTOS = os.path.join('uplproductos')
