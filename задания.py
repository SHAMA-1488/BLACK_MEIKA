#задание 1
from datetime import datetime

data = {
    "username":"Ivan",
    "created_at": datetime.now().isoformat()
}

import json
json.dumps(data)

data2 =["phyton","api","json"]
json.dumps(data2)
class DB_CONN:
    def __init__(self):
        pass

class User:
    def __init__(self, username,pasword):
        self.username = username
        self.__pasword = self.__hash__()       
        self.__db_session = DB_CONN()
        self.created_at = datetime.now()
    def to_dict(self):
        return {"username":self.username,
                "create_at":self.created_at.isoformat()}
    
user = User("ivan", "secret")

with open("user_data.json","w",encoding="utf-8")as json_file:
          json.dump(user.to_dict(), json_file)