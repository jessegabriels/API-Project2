from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["argon2", "bcrypt"], deprecated="auto")


def get_gamemode_key_hash(gamemode_key):
    return pwd_context.hash(gamemode_key)

