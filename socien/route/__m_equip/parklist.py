from flask import request               #공원list
from flask_restx import Resource, Api, Namespace, fields, reqparse, inputs
from ._m_equip import Mequip
import app             
from sqlalchemy import text


@Mequip.route('/parklist') 
class ParkList(Resource):
    @Mequip.response(200, 'Success')              
    @Mequip.response(500, 'Internal Server Error')
    def get(self):

        sql = 'SELECT * FROM park'
        rows = app.app.database.execute(text(sql),).fetchall()
        #rows에 쿼리실행한 결과들 fetchall로 모두 저장 
        
        retVal = [] 
        for row in rows: #쿼리실행결과들에서 row에 하나씩 불러온다
            r = {        #row에 있는 정보를 r에 딕트로 저장하고 r을 위에 생성해둔 retval=[]에 append한다 
                    'p_id'     : row['p_id'],
                    'p_name'   : row['p_name'],
                    'x'        : row['x'],
                    'y'        : row['y'],
                    'website'  : row['website']                   
                }
            retVal.append(r)

        return {                 #get함수의 결과로 clinet에 다음 형식으로 리턴한다.      
            'code':'successs',   #json형태이며 응답에 retval을 넣어준다.
            'message':'',
            'response': {
                'List': retVal
            }
        }, 200