from flask import request             #공원id -> 해당 공원의 운동기구list
from flask_restx import Resource, Api, Namespace, fields, reqparse, inputs
from sqlalchemy.sql.type_api import NULLTYPE
from ._m_equip import Mequip
import app
from sqlalchemy import text


parser = reqparse.RequestParser()
parser.add_argument('id', help='공원 ID', type=int, required=True)

@Mequip.route('/p_e_list')
class P_E_List(Resource):
    @Mequip.expect(parser)
    @Mequip.response(200, 'Success')
    @Mequip.response(500, 'Internal Server Error')
    def get(self):
        args = parser.parse_args()
        id = args['id']

        sql = 'SELECT * FROM equip WHERE p_id=:id'
        query = {
            'id': id
        }
        rows = app.app.database.execute(text(sql), query).fetchall()

        if rows == None:
            return {
                'code': 'error',
                'message': 'p_id가 잘못되었습니다.'
            }, 500
            
        retVal = [] 
        for row in rows: #쿼리실행결과들에서 row에 하나씩 불러온다
            r = {        #row에 있는 정보를 r에 딕트로 저장하고 r을 위에 생성해둔 retval=[]에 append한다 
                    'e_id'     : row['e_id'],
                    'p_id'     : row['p_id'],
                    'e_name'   : row['e_name'],
                    'category' : row['category']
                }
            retVal.append(r)
        

        return {                 #get함수의 결과로 clinet에 다음 형식으로 리턴한다.      
            'code':'successs',   #json형태이며 응답에 retval을 넣어준다.
            'message':'',
            'response': {
                'List': retVal
            }
        }, 200

        
        
        
