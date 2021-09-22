from flask import Blueprint

# from controllers.SalidaController import index, store, show, update, destroy, create, edit
from controllers.SalidaController import index, store, destroy

salida_bp = Blueprint('salida_bp', __name__, template_folder='templates/salida')
salida_bp.route('/', methods=['GET'])(index)
# salida_bp.route('/create', methods=['GET'])(create)
# salida_bp.route('edit/<int:salida_id>', methods=['GET'])(edit)
salida_bp.route('/store', methods=['POST'])(store)
# salida_bp.route('/<int:salida_id>', methods=['GET'])(show)
# salida_bp.route('/update', methods=['POST'])(update)
salida_bp.route('/destroy/<int:salida_id>', methods=['GET', 'POST','DELETE'])(destroy)

