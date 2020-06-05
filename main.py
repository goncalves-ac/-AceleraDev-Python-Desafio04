import jwt


def create_token(data, secret):
    token = jwt.encode(data, secret, 'HS256')
    return token

def verify_signature(token):
    try:
        decifrar = jwt.decode(token, 'acelera')
        return decifrar
    except:
        return {"error": 2}
