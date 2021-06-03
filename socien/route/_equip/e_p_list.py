from flask import request             #운동기구 이름-> 관련 공원의 위치 list를 얻어오는 파일입니다.
from flask_restx import Resource, Api, Namespace, fields, reqparse, inputs
from .equip import Equip
import app
from sqlalchemy import text

parser = reqparse.RequestParser()
parser.add_argument('e_name', help='운동기구 이름', type=str, required=True)

@Equip.route('/list')
class EquipList(Resource):
    @Equip.expect(parser)
    @Equip.response(200, 'Success')
    @Equip.response(500, 'Internal Server Error')
    def get(self):
        args = parser.parse_args()
        id = args['e_name']
        
        #equip 테이블을 기준으로 park테이블과 조인하여 해당 운동기구가 있는 공원 좌표를 얻어온다.
        sql = 'SELECT e_id,e_name,x,y,p_name FROM equip LEFT JOIN park ON equip.p_id = park.p_id WHERE e_name= :e_name'
        query = {
            'e_name': id
        }
        rows = app.app.database.execute(text(sql), query).fetchall()

        retVal = [] 
        for row in rows: #쿼리실행결과들에서 row에 하나씩 불러온다
            r = {        #row에 있는 정보를 r에 딕트로 저장하고 r을 위에 생성해둔 retval=[]에 append한다 
                   'e_id'     : row['e_id'],
                    'e_name'   : row['e_name'],
                    'x'     : row['x'],
                    'y'     : row['y'],
                    'p_name'   : row['p_name']                                 
                }
            retVal.append(r)

        if rows == None:
            return {
                'code': 'error',
                'message': 'id가 잘못되었습니다.'
            }, 500


        return { 
            'response': retVal     
        }, 200

