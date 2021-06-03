from flask import request             #처리가 완료된 신고접수를 삭제하는 API입니다.
from flask_restx import Resource, Api, Namespace, fields, reqparse, inputs
from ._m_report import Mreport
import app
from sqlalchemy import text

#r_id로 삭제합니다.
parser = reqparse.RequestParser()
parser.add_argument('r_id', help='신고 ID', type=int, required=True)

@Mreport.route('/delete')
class Report_Delete(Resource):
    @Mreport.expect(parser)
    @Mreport.response(200, 'Success')
    @Mreport.response(500, 'Internal Server Error')
    def get(self):
        args = parser.parse_args()
        r_id = args['r_id']

        sql = 'DELETE FROM report WHERE  r_id = :r_id'
        query = {
            'r_id': r_id
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
        
        
