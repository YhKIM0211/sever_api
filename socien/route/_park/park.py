from flask_restx import Namespace

Park = Namespace(name= 'park', description='공원 관련 API') #import

# API Import
from . import list
