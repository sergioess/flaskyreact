from flask import Blueprint

from controllers.ProductoController import index, store, show, update, destroy, create, edit

producto_bp = Blueprint('producto_bp', __name__, template_folder='templates/productos')
producto_bp.route('/', methods=['GET'])(index)
producto_bp.route('/create', methods=['GET'])(create)
producto_bp.route('edit/<int:producto_id>', methods=['GET'])(edit)
producto_bp.route('/store', methods=['POST'])(store)
producto_bp.route('/<int:producto_id>', methods=['GET'])(show)
producto_bp.route('/update', methods=['POST'])(update)
producto_bp.route('/destroy/<int:producto_id>', methods=['GET', 'POST','DELETE'])(destroy)
