from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, url_for
from flask_cors import CORS

from routes.categoria_bp import categoria_bp

# from flask_mongoalchemy import MongoAlchemy

from flask import send_from_directory


app = Flask(__name__)
app.config.from_object('config')
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://oxwttxarfidlxi:89e47cacfc5926776ab52a7e485b08a91bf9632736ca0843d80b6356b506f3f2@ec2-3-231-69-204.compute-1.amazonaws.com:5432/d3hr8qndm4p50h'
db = SQLAlchemy(app)


app.register_blueprint(categoria_bp, url_prefix='/categoria')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/uploads/<nombreFoto>')
def uploads(nombreFoto):
    return send_from_directory(app.config['CARPETA'], nombreFoto)


@app.route('/uplproductos/<nombreFoto>')
def uplproductos(nombreFoto):
    return send_from_directory(app.config['CARPETA_PTOS'], nombreFoto)


if __name__ == '__main__':
    app.run(debug=True)
