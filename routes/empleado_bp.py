from flask import Blueprint

from controllers.EmpleadoController import index, store, show, update, destroy, create, edit

empleado_bp = Blueprint('empleado_bp', __name__, template_folder='templates/empleados')
empleado_bp.route('/', methods=['GET'])(index)
empleado_bp.route('/create', methods=['GET'])(create)
empleado_bp.route('edit/<int:empleado_id>', methods=['GET'])(edit)
empleado_bp.route('/store', methods=['POST'])(store)
empleado_bp.route('/<int:empleado_id>', methods=['GET'])(show)
empleado_bp.route('/update', methods=['POST'])(update)
empleado_bp.route('/destroy/<int:empleado_id>', methods=['GET', 'POST','DELETE'])(destroy)
