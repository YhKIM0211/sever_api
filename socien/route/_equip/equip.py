from flask_restx import Namespace

Equip = Namespace(name='equip', description='운동기구 관련 API') #import

# API Import
from . import e_p_list