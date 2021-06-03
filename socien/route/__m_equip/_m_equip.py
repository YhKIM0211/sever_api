from flask_restx import Namespace

Mequip = Namespace(name='manager_equip', description='관리자페이지 운동기구 관련 API') #import

# API Import
from . import delete #운동기구 삭제 
from . import insert #운동기구 생성 
from . import put    #운동기구 수정 
from . import parklist #공원 리스트보내준다. 
from . import p_e_list   #공원id -> 해당 공원의 운동기구 리스트 조회