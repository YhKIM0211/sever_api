from flask import request            #신고list를 얻어오는 API입니다
from flask_restx import Resource, Api, Namespace, fields, reqparse, inputs
from ._m_report import Mreport
import app             
from sqlalchemy import text



@Mreport.route('/list') 
class REPORT_List(Resource):
    @Mreport.response(200, 'Success')               #성공시 응답 200
    @Mreport.response(500, 'Internal Server Error') #실패시 응답 500
    def get(self):
                
        sql = 'SELECT * FROM report'
        rows = app.app.database.execute(text(sql),).fetchall()
        #rows에 쿼리실행한 결과들 fetchall로 모두 저장 
        
        retVal = [] 
        for row in rows: #쿼리실행결과들에서 row에 하나씩 불러온다
            r = {        #row에 있는 정보를 r에 딕트로 저장하고 r을 위에 생성해둔 retval=[]에 append한다                    
                    'r_id'        : row['r_id'],
                    'p_name'      : row['p_name'],
                    'r_text'      : row['r_text'],
                    'r_phone'     : row['r_phone'],
                    'r_name'      : row['r_name'],
                    'r_date'      : row['r_date']
                }
            retVal.append(r)

        return {                 
            'code'    :'successs',   
            'message' :'',
            'response': {
                'List': retVal
            }
        }, 200