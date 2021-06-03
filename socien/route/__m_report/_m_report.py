from flask_restx import Namespace

Mreport = Namespace(name='manager_report', description='관리자 신고관리 API') #import

# API Import
from . import list   #신고 리스트
from . import delete #처리 완료된 신고목록 삭제  
from . import website #신고를 처리할 민원접수 웹사이트 얻어오는 api
                     