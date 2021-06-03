from flask import Flask,  render_template #####고침 web을 위한 테스트
from flask_restx import Resource, Api
from flask_cors import CORS            #origin 문제 해결을 위해 설치
from sqlalchemy import create_engine   #데이터 베이스 연결을 위한 환경설정
from route._park.park import Park           
from route._equip.equip import Equip
from route._report.report import Report
from route.__m_report._m_report import Mreport
from route.__m_equip._m_equip import Mequip
#from 라우팅 폴더.park폴더.park파일 로부터 
# import park파일을 보면 park관련 네임스페이스(/park)를 저장하기위해 Park변수에 넣어주었으므로 이를 불러옵니다. 
###다른 폴더 만들때 위의 방식으로 추가

URL_PREFIX = '/api/v1'  

app = Flask(__name__)
CORS(app)
api = Api(
    app,
    version='1.0',
    title='Socien API',
    description='Green Gym API'
)

### add namespace 
api.add_namespace(Park, URL_PREFIX + "/park") ####
api.add_namespace(Equip, URL_PREFIX + "/equip") ####
api.add_namespace(Report, URL_PREFIX + "/report") ####
api.add_namespace(Mreport,URL_PREFIX + "/manager_report")
api.add_namespace(Mequip,URL_PREFIX + "/manager_equip")

# DB 연결
test_config=None

if test_config is None:      
    app.config.from_pyfile("config.py") #cofig.py파일의 db이름을 주의하기
else:
    app.config.update(test_config)

database = create_engine(app.config['DB_URL'], encoding = 'utf-8', max_overflow = 0)   
app.database = database


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)