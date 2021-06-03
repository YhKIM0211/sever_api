from flask import request             #한개의 공원 위치를 얻어오는 파일입니다.
from flask_restx import Resource, Api, Namespace, fields, reqparse, inputs
from .park import Park
import app
from sqlalchemy import text


parser = reqparse.RequestParser()
parser.add_argument('id', help='공원 ID', type=int, required=True)

@Park.route('/detail')
class ParkDetail(Resource):
    @Park.expect(parser)
    @Park.response(200, 'Success')
    @Park.response(500, 'Internal Server Error')
    def get(self):
        args = parser.parse_args()
        id = args['id']

        sql = 'SELECT * FROM park WHERE p_id=:id'
        query = {
            'id': id
        }
        row = app.app.database.execute(text(sql), query).fetchone()

        if row == None:
            return {
                'code': 'error',
                'message': 'id가 잘못되었습니다.'
            }, 500

        r = {
            'p_id':row['p_id'],
            'p_name':row['p_name'],
            'x': row['x'],
            'y': row['y'],
            'website': row['website']
        }
        
        return {
            'code':'successs',
            'message':'',
            'response': {
                'detail': r
            }
        }, 200

