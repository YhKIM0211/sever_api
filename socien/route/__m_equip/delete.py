from flask import request             
from flask_restx import Resource, Api, Namespace, fields, reqparse, inputs
from ._m_equip import Mequip
import app
from sqlalchemy import text

#운동기구 id로 삭제합니다.
parser = reqparse.RequestParser()
parser.add_argument('e_id', help='운동기구 ID', type=int, required=True)

@Mequip.route('/delete')
class E_DELETE(Resource):
    @Mequip.expect(parser)
    @Mequip.response(200, 'Success')
    @Mequip.response(500, 'Internal Server Error')
    def get(self):
        args = parser.parse_args()
        e_id = args['e_id']
        
        sql = 'DELETE FROM equip WHERE  e_id = :e_id'
        query = {
            'e_id': e_id
        }
        row = app.app.database.execute(text(sql), query)


        if row == None:
            return {
                'code': 'error',
                'message': 'id가 잘못되었습니다.'
            }, 500

        return {
            'code':'successs',
            'message':'',
        }, 200

       



        
        
        
