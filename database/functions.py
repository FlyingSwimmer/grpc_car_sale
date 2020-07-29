from database import connection
from database.models import User



def get_user(session, username, password):
    user = session.query(User).filter(User.username==username).first()
    print("user_getter: ", user)
    if user and user.check_password(password):
        return user
    return None