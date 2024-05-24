from datetime import datetime, timedelta, timezone
import jwt

# Chave secreta para assinar os tokens
SECRET_KEY = 'django-insecure-x*(q3p^1)e-&sa@q89judj%=or7f8bht7xr)!qh5ppi*d*345j'

def generate_jwt_token(user_id):
    # Define o payload do token
    payload = {
        'user_id': user_id,
        'exp': datetime.now(timezone.utc) + timedelta(minutes=15)  # Tempo de expiração do token
    }
    # Gera o token JWT
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token

def verify_jwt_token(token):
    try:
        # Decodifica o token
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        # Token expirado
        return {'error': 'Token expirado'}
    except jwt.InvalidTokenError:
        # Token inválido
        return {'error': 'Token inválido'}
