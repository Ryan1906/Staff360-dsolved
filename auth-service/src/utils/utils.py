import bcrypt

def generate_hash(password: str) -> str:
    '''Genera un hash del password usando bcrypt.'''
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode()

def verify_hash(password: str, hashed: str) -> bool:
    '''Verifica si el password es el correcto'''
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

