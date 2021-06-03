#list 파일은 사용자 기준 1km의 공원리스트를 돌려주는 api이다.
from flask import request 
from flask_restx import Resource, Api, Namespace, fields, reqparse, inputs
from .park import Park  #park.py파일의 네임스페이스를 이용하기 때문에 
import app
from sqlalchemy import text #sql문을 해석하기 위한 환경설정
from math import sin, cos, sqrt, atan2, radians #거리계산 함수를 이용하기 위한 환경설정

parser = reqparse.RequestParser() 
#위의 코드는 flask_restx의 reqparse 기능을 임포트 했으므로 여기서 제공해주는 RequestParser()를 사용하기위해 parser에 메소드 저장 
parser.add_argument('x', help='경도', type=float, required=True) 
#.add_argument('x')는 post의 body 값에서 해당 키의 값('x': 값)을 받아서 저장 합니다.
parser.add_argument('y', help='위도', type=float, required=True)
parser.add_argument('dist', help='거리', type=float, required=True, default=1) #dist값이 없으면 1로

#distLL : 거리계산 함수 
def distLL(x1, y1, x2, y2): #사용자의 위도 경도 위치를 받고 x1 y1 공원의 위치x2 y2와의 거리를 계산합니다.
    R = 6373.0
    lat1 = radians(y1) 
    lon1 = radians(x1) 
    lat2 = radians(y2) 
    lon2 = radians(x2) 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2 
    c = 2 * atan2(sqrt(a), sqrt(1 - a)) 
    distance = R * c

    return distance # 계산한 거리 값 리턴

#라우팅! http://0.0.0.0:8000/park 가 기본 주소

#@Park는 네임스페이스 참조로 '/park'를 포함한다.
@Park.route('/list')  #http://0.0.0.0:8000/park/list 
class ParkList(Resource):
    @Park.expect(parser) #사용 인자는 parser에서 받은 인자들이다 #https://flask-restplus.readthedocs.io/en/stable/swagger.html 설명 참조하기
    @Park.response(200, 'Success') #성공시 응답 200
    @Park.response(500, 'Internal Server Error') #실패시 응답 500
    def get(self):
        args = parser.parse_args() #parse_args() returns a 'Python dictionary' instead of a custom data structure.
        x = args['x']     #변수에 받은 인자 값 저장 -> 위에서 딕셔너리 형태로 args변수에 넘김 args에서 각key 'x'의 :값을 받음
        y = args['y']
        dist = args['dist']

        #SQL 이용 안함                     #sql 변수에 스트링형태의 sql쿼리문 저장
        sql = 'SELECT * FROM park WHERE 1' #1은 항상 조건이 참이라는 의미 
        rows = app.app.database.execute(text(sql), {}).fetchall() #rows에 쿼리실행한 결과들 fetchall로 모두 저장 
        
        retVal = [] 
        for row in rows: #쿼리실행결과들 애서 row에 하나씩 불러온다
            px = float(row['x']) #db에서 스트링으로 넘어온 값을 float으로 바꾼다
            py = float(row['y'])
            ud = distLL(x,y,px,py) #함수불러와서 거리 계산
            if ud <= dist: #거리가 기본 값인 1km보다 작다면 사용자 기준 1km반경에 있는 공원이므로 
                r = {                            #row에 있는 정보를 r에 딕트로 저장하고 r을 위에 생성해둔 retval=[]에 append한다 
                    'p_id':row['p_id'],
                    'p_name':row['p_name'],
                    'x': px,
                    'y': py,
                    'website': row['website']
                }
                retVal.append(r)

        return {                 #get함수의 결과로 clinet에 다음 형식으로 리턴한다.      
            'code':'successs',   #json형태이며  응답에 1km 공원리스트인 retval을 넣어준다.
            'message':'',
            'response': {
                'List': retVal
            }
        }, 200

