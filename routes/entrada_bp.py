from flask import Blueprint

# from controllers.EntradasController import index, store, show, update, destroy, create, edit
from controllers.EntradasController import index, store, destroy

entrada_bp = Blueprint('entrada_bp', __name__, template_folder='templates/entrada')
entrada_bp.route('/', methods=['GET'])(index)
# entrada_bp.route('/create', methods=['GET'])(create)
# entrada_bp.route('edit/<int:entrada_id>', methods=['GET'])(edit)
entrada_bp.route('/store', methods=['POST'])(store)
# entrada_bp.route('/<int:entrada_id>', methods=['GET'])(show)
# entrada_bp.route('/update', methods=['POST'])(update)
entrada_bp.route('/destroy/<int:entrada_id>', methods=['GET', 'POST','DELETE'])(destroy)
