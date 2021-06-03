from flask import request            
from flask_restx import Resource, Api, Namespace, fields, reqparse, inputs
from .report import Report ###
import app
from sqlalchemy import text

#post 공원이름,신고글,사용자이름,사용자 번호,신고 날짜 
parser = reqparse.RequestParser() 
parser.add_argument('p_name', help='신고 접수하는 공원 이름', type=str, required=True)
parser.add_argument('r_text', help='신고 글', type=str, required=True) 
parser.add_argument('r_phone', help='신고자 전화번호', type=str, required=True)
parser.add_argument('r_name', help='신고자 이름', type=str, required=True)
parser.add_argument('r_date', help='신고 날짜', type=str, required=True)


@Report.route('/insert',methods=['POST']) ####
class ReportInsert(Resource):
    @Report.expect(parser)
    @Report.response(200, 'Success')
    @Report.response(500, 'Internal Server Error')
    def post(self):
        args = parser.parse_args()
        
        p_name = args['p_name']
        r_text = args['r_text']
        r_phone = args['r_phone']
        r_name = args['r_name']
        r_date = args['r_date']

        sql = 'INSERT INTO report(p_name, r_text, r_phone, r_name, r_date) VALUES ( :p_name, :r_text, :r_phone, :r_name, :r_date)'
        query = {
            'p_name': p_name,     
            'r_text': r_text,
            'r_phone':r_phone,
            'r_name':r_name,
            'r_date':r_date
        }
        app.app.database.execute(text(sql), query) #쿼리 실행       

        return {
            'code':'successs',
            'message':'',
        }, 200

