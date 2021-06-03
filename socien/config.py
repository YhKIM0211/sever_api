db = {
    'user'     : 'green2',		
    'password' : 'root',		
    'host'     : '127.0.0.1',	
    'port'     : 3306,			
    'database' : 'GreenGym'		
}

DB_URL = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8"
