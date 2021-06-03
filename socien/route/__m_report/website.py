from flask import request            
from flask_restx import Resource, Api, Namespace, fields, reqparse, inputs
from ._m_report import Mreport
import app
from sqlalchemy import text


parser = reqparse.RequestParser()
parser.add_argument('r_id', help='신고 ID', type=int, required=True)

@Mreport.route('/website') 
class WEBSITE(Resource):
    @Mreport.expect(parser)
    @Mreport.response(200, 'Success')
    @Mreport.response(500, 'Internal Server Error')
    def get(self):
        args = parser.parse_args()
        id = args['r_id']

        #report 테이블을 기준으로 park테이블과 조인하여 신고접수된 공원의 민원을 처리하는 사이트주소를 얻어온다.
        sql = 'SELECT r_id, report.p_name,website FROM report LEFT JOIN park ON report.p_name = park.p_name WHERE r_id= :r_id'
        query = {
            'r_id': id
        }
        row = app.app.database.execute(text(sql), query).fetchone()

        if row == None:
            return {
                'code': 'error',
                'message': 'id가 잘못되었습니다.'
            }, 500

        r = { 
                    'r_id'     : row['r_id'],
                    'p_name'     : row['p_name'],
                    'website'   : row['website']                
        }
        
        return {
            'code':'successs',
            'message':'',
            'response': {
                'detail': r
            }
        }, 200

