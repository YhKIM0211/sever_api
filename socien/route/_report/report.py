from flask_restx import Namespace

Report = Namespace(name='report', description='고장 신고 관련 API') #import

# API Import
from . import insert #앱사용자- 고장신고 등록 api -POST
