from flask import request            
from flask_restx import Resource, Api, Namespace, fields, reqparse, inputs
from ._m_equip import Mequip
import app
from sqlalchemy import text

#post 운동기구id, 공원id, 운동기구 이름, 운동기구 종류 
parser = reqparse.RequestParser() 
parser.add_argument('e_id', help='운동기구 id', type=int, required=True)
parser.add_argument('p_id', help='운동기구가 있는 공원 id', type=int, required=True)
parser.add_argument('e_name', help='운동기구 이름', type=str, required=True)
parser.add_argument('category', help='운동기구 종류', type=str, required=True)


@Mequip.route('/put',methods=['POST']) 
class PUT(Resource):
    @Mequip.expect(parser)
    @Mequip.response(200, 'Success')
    @Mequip.response(500, 'Internal Server Error')
    def post(self):
        args = parser.parse_args()
        
        e_id = args['e_id']
        p_id = args['p_id']
        e_name = args['e_name']
        category = args['category']

        #운동기구 id로 수정합니다.
        sql = 'UPDATE equip SET p_id = :p_id, e_name = :e_name, category = :category WHERE e_id = :e_id'
        query = {
            'e_id': e_id,
            'p_id': p_id,     #실제 쿼리 컬럼에 값으로 매핑되는 받아온 인자 값들
            'e_name':e_name,
            'category':category
        }
        app.app.database.execute(text(sql), query) #쿼리 실행       

        return {
            'code':'successs',
            'message':'',
        }, 200