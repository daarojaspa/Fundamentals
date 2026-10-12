import bcrypt

def hash_password(password: str) -> str:
    pw = password.encode("utf-8")[:72]          # enforce the limit yourself
    return bcrypt.hashpw(pw, bcrypt.gensalt()).decode()

def verify_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode("utf-8")[:72], hashed.encode())
