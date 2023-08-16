#!/usr/bin/env python3
"""user authentication service to hash passwords"""
import bcrypt
from db import DB
from user import User, Base
from sqlalchemy.orm.exc import NoResultFound



def _hash_password(password: str) -> bytes:
    """hashing the password using bcrypt"""
    encode_password = password.encode()
    return bcrypt.hashpw(encode_password, bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """registering new user"""
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            hashed = _hash_password(password)
            user = self._db.add_user(email, hashed)
            return user
        raise ValueError(f"User {email} already exists")
