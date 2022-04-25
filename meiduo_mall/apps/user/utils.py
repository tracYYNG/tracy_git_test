from itsdangerous import URLSafeTimedSerializer  as Serializer
# URLSafeTimedSerializer 
from meiduo_mall import settings

def create_token(user_id):
    auth_s = Serializer(secret_key=settings.SECRET_KEY)
    token = auth_s.dumps({'user_id':user_id})
    return token

def check_token(token):
    auth_s = Serializer(secret_key=settings.SECRET_KEY)
    user_id = auth_s.loads(token)
    return user_id