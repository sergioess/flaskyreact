from flask import Flask
# from app import db
import conn

import psycopg2
from psycopg2.extras import RealDictCursor

from flask import config, render_template, redirect, url_for, request, abort, flash, jsonify


app = Flask(__name__)


class Categoria:

    id = 0
    nombre = ''
    id_tienda = 1
    activo = 1

    # clasificaciones = []  # Atributo de la clase categorias

    cantidadClasificaciones = 0

    # def __init__(self, cantidadClasificaciones):
    #     self.cantidadClasificaciones = cantidadClasificaciones

    def __init__(self):
        pass

    def __init__(self, nombre):
        print(nombre)
        self.nombre = nombre
        pass

    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        pass

    @staticmethod
    def listClasificacion():

        conn = psycopg2.connect(
            host='ec2-3-231-69-204.compute-1.amazonaws.com', port=5432, database='d3hr8qndm4p50h', user='oxwttxarfidlxi', password='89e47cacfc5926776ab52a7e485b08a91bf9632736ca0843d80b6356b506f3f2')
        cur = conn.cursor()
        query_sql = "SELECT id, nombre, id_tienda, activo FROM categorias where activo = 1"
        cur.execute(query_sql)
        # clasificaciones = cur.fetchall()
        # print(clasificaciones)

        columns = ('id', 'nombre', 'id_tienda', 'activo')

        results = []
        for row in cur.fetchall():
            results.append(dict(zip(columns, row)))

        cur.close()
        conn.commit()
        return results
        # return clasificaciones

    def create_clasificacion(self):
        # print(self.nombre)
        try:
            connection = conn.create_connection()
            cur = connection.cursor()
            cur.execute(
                "INSERT INTO categorias (nombre, id_tienda, activo) VALUES ('%s', 1, 1)" % (self.nombre))
            # cur.execute(
            #     "INSERT INTO clasificaciones (nombre, id_tienda, activo) VALUES (%s,1,1)", (self.nombre))
            connection.commit()
        finally:
            cur.close()
            connection.close()

    def delete(self):
        try:
            print(self.id)

            connection = conn.create_connection()
            cur = connection.cursor()
            cur.execute(
                "UPDATE categorias SET activo = 0 WHERE id = %d" % (self.id))
            connection.commit()
        finally:
            cur.close()
            connection.close()

    def update(self):
        try:
            connection = conn.create_connection()
            cur = connection.cursor()

            cur.execute(
                "UPDATE categorias SET nombre = %s WHERE id = %s", (self.nombre, self.id))
            connection.commit()
        finally:
            cur.close()
            connection.close()

    def edit(self):
        try:
            connection = conn.create_connection()
            cur = connection.cursor()

            cur.execute(
                "UPDATE categorias SET nombre = %s WHERE id = %s", (self.nombre, self.id))
            connection.commit()
        finally:
            cur.close()
            connection.close()

    def get_nombre(self):
        try:
            connection = conn.create_connection()
            cur = connection.cursor()
            cur.execute(
                "SELECT * FROM categorias WHERE nombre='%s'" % (self.nombre))

            clasificacion = cur.fetchone()
            self.id = clasificacion[0]
            self.nombre = clasificacion[1]

        finally:
            cur.close()
            connection.close()
