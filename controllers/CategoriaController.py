import sys
from flask import Flask
from flask import config, render_template, redirect, url_for, request, abort, flash, jsonify
from datetime import datetime
# from flask_marshmallow import Marshmallow
# from marshmallow import fields
import os
import json


from models.Categoria import Categoria

app = Flask(__name__)
app.config.from_object('config')
# ma = Marshmallow(app)


def index():
    listaClasificaciones = Categoria.listClasificacion()
    # print(listaClasificaciones)
    # return categoria_schema.jsonify(listaClasificaciones[1])
    # return categoria_schema.jsonify(Categoria.listaClasificaciones)
    # return listaClasificaciones
    return json.dumps(listaClasificaciones, indent=2)
    # return render_template('/categoria/index.html', clasificaciones=listaClasificaciones)


def create():
    return render_template('/categoria/create.html')


def update(clasificacion_id):
    if request.method == 'PUT':
        _nombre = request.form.get('txtNombre')
        _id = request.form.get('txtId')

        categoriaEditar = Categoria(_id, _nombre)
        categoriaEditar.edit()
    return json.dumps(categoriaEditar, indent=2)
    # return redirect('/categoria')


def store():

    if request.method == 'POST':
        _nombre = request.form.get('txtNombre')

        if(_nombre == ''):
            flash('Recuerda llenar los datos de los campos')
            return redirect(url_for('empleado_bp.create'))
        # print(_nombre)
        categoriaNueva = Categoria(1, _nombre)
        categoriaNueva.create_clasificacion()

    return redirect('/categoria')


def show(clasificacion_id):
    return render_template('/categoria/index.html')


def destroy(clasificacion_id):
    # print(clasificacion_id)
    categoriaBorrar = Categoria(clasificacion_id, "borrar")
    categoriaBorrar.delete()
    return redirect('/categoria')


# class CategoriaSchema(ma.Schema):
#     # class Meta:
#     #     fields = ('id', 'nombre', 'id_tienda', 'activo')
#     id = fields.Integer(dump_only=True)
#     nombre = fields.String()
#     id_tienda = fields.Integer()
#     activo = fields.Integer()


# categoria_schema = CategoriaSchema()
# categorias_schema = CategoriaSchema(many=True)
