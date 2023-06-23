from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()
db_connection_string = os.getenv('DB_CONNECTION_STRING')

engine = create_engine(db_connection_string)


def load_user_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from users"))

        result_all = []
        for row in result.all():
            result_all.append(dict(row))
        return result_all
    
def load_video_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(text("select * from users WHERE user_id = :val"), val=id)
        rows = result.all()
        if len(rows) == 0:
            return None
        else:
            return dict(rows[0])
        
def add_user_to_db(data):
    with engine.connect() as conn:
        query = text("INSERT INTO users(firstname, username, password, email) VALUES(:firstname, :username, :password, :email)")

        conn.execute(query, firstname=data['firstname'], username=data['username'],password=data['password'],email=data['email'])











    # print(result_all)
    # print(result.all())
    # print(type(result.all()))
    # result_all = result.all()
    
    # first = result_all[1]
    # print(type(first))
