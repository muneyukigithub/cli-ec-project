from dataclasses import dataclass

@dataclass
class User:
    """ユーザー管理クラス"""
    user_id:int = None
    session_id:str = None
    username:str = "Guest"
    is_logged_in:bool = False

    def reset_data(self):
        self.username = "Guest"
        self.session_id = None
        self.user_id = None