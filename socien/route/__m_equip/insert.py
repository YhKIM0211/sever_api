from flask import request            
from flask_restx import Resource, Api, Namespace, fields, reqparse, inputs
from ._m_equip import Mequip
import app
from sqlalchemy import text

#post  
parser = reqparse.RequestParser() 
parser.add_argument('p_id', help='운동기구가 있는 공원 id', type=int, required=True)
parser.add_argument('e_name', help='운동기구 이름', type=str, required=True)
parser.add_argument('category', help='운동기구 종류', type=str, required=True)


@Mequip.route('/insert',methods=['POST']) 
class E_Insert(Resource):
    @Mequip.expect(parser)
    @Mequip.response(200, 'Success')
    @Mequip.response(500, 'Internal Server Error')
    def post(self):
        args = parser.parse_args()
        
        p_id = args['p_id']
        e_name = args['e_name']
        category = args['category']

        sql = 'INSERT INTO equip(p_id, e_name, category) VALUES ( :p_id, :e_name, :category)'
        query = {
            'p_id': p_id,     
            'e_name':e_name,
            'category':category
        }
        app.app.database.execute(text(sql), query) #쿼리 실행       

        return {
            'code':'successs',
            'message':'',
        }, 200

