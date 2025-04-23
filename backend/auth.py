import jwt
from datetime import datetime, timedelta

SEGREDO = "segredo_supersecreto"

def gerar_token(usuario):
    payload = {
        "usuario": usuario,
        "exp": datetime.utcnow() + timedelta(hours=1)
    }
    return jwt.encode(payload, SEGREDO, algorithm="HS256")

def validar_token(token):
    try:
        jwt.decode(token, SEGREDO, algorithms=["HS256"])
        return True
    except jwt.ExpiredSignatureError:
        return False
    except jwt.InvalidTokenError:
        return False
