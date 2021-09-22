from flask import Blueprint

from controllers.CategoriaController import index, store, show, update, destroy, create

categoria_bp = Blueprint(
    'categoria_bp', __name__, template_folder='templates/categoria')
categoria_bp.route('/', methods=['GET'])(index)
categoria_bp.route('/create', methods=['GET'])(create)
categoria_bp.route('/store', methods=['POST'])(store)
categoria_bp.route('/<int:clasificacion_id>', methods=['GET'])(show)
categoria_bp.route('/update/<int:clasificacion_id>', methods=['PUT'])(update)
categoria_bp.route('/destroy/<int:clasificacion_id>',
                   methods=['GET', 'POST', 'DELETE'])(destroy)
