from dataclasses import dataclass
from model import UserModel,SessionModel
from model import session
from datetime import datetime, timedelta
from sqlalchemy.exc import DatabaseError
import uuid

class Auth:
    """認証系の処理を管理するクラス"""
    def __init__(self,user):
        self.user = user

    def signup(self):
        try:
            userdata = self.input_userdata() 
            self.create_user(userdata)
            return True
        except ValueError as e:
            print(f"空の入力値があります")
        except Exception as e:
            print("エラーが発生しました")
        return False

    
    def input_userdata(self):
               
        username = input("ユーザ名を入力してください: ")
        password = input("パスワードを入力してください: ")
        email = input("メールアドレスを入力してください: ")
        phonenumber = input("電話番号を入力してください: ")

        if not (username and password and email and phonenumber):
            raise ValueError("入力値不正")

        userdata = {
            "username":username,
            "password":password,
            "email":email,
            "phonenumber":phonenumber,
            "is_active":0,
            "role":0
        }

        return userdata

    def create_user(self,user_data):
        try:
            query = UserModel(**user_data)
            session.add(query)
            session.commit()
        except DatabaseError as e:
            raise 
        except Exception as e:
            raise


    def basic_login(self):

        try:
            username,password = self.input_logindata()
            user = self.basic_authenticate(username,password)

            sessionid = self.create_session(user)

            if user and sessionid:
                set_data={
                    "user_id":user.id,
                    "username":user.username,
                    "session_id":sessionid
                }
                self.set_user(self.user ,**set_data)
                return True
        except ValueError as e:
            print(f"空の入力値があります")
        except Exception as e:
            print("エラーが発生しました",e)
        
        return False

    def input_logindata(self):
        username = input("ユーザ名を入力してください: ")
        password = input("パスワードを入力してください: ")

        if not (username and password):
            raise ValueError

        return username,password

    def basic_authenticate(self, username, password):
        
        user = session.query(UserModel).filter_by(username=username).first()

        if user is None or not (username == user.username and password == user.password):
            return None

        return user

    def set_user(self,user,**kwargs):

            for key,value in kwargs.items():
                setattr(user, key, value)

    def create_session(self,user):
        try:
            if user:
                session_id = self.generate_session()
                self.save_session(session_id, user.id)
            return session_id            

        except Exception as e:
            raise 

    def save_session(self,session_id,user_id):
        expiration = datetime.now() + timedelta(days=1)
        query = SessionModel(session_id=session_id,user_id=user_id,expiration=expiration)
        session.add(query)
        session.commit()

    def generate_session(self):
        return str(uuid.uuid4())


    def logout(self):
        try:
            self.delete_session()
            self.user.reset_data()
            print("ログアウトしました")
        except Exception as e:
            print("ログアウト失敗しました")
    
    def delete_session(self):
        session_id = session.query(SessionModel).filter_by(session_id=self.user.session_id).first()
        session.delete(session_id)
        session.commit()
