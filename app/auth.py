from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["argon2", "bcrypt"], deprecated="auto")


def get_location_hash(location):
    return pwd_context.hash(location)

