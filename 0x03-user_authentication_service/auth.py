#!/usr/bin/env python3
"""user authentication service to hash passwords"""
import bcrypt
from db import DB
from user import User, Base
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4
from typing import Union


def _hash_password(password: str) -> bytes:
    """hashing the password using bcrypt"""
    encode_password = password.encode()
    return bcrypt.hashpw(encode_password, bcrypt.gensalt())


def _generate_uuid() -> str:
    """returning the uuid4 string"""
    return str(uuid4())


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

    def valid_login(self, email: str, password: str) -> bool:
        """checking if login is valid"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        user_pass = user.hashed_password
        passwd = password.encode('utf-8')
        return bcrypt.checkpw(passwd, user_pass)

    def create_session(self, email: str) -> str:
        """creating the session id for the login users"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        session_id = _generate_uuid()
        self._db.update_user(user.id, session_id=session_id)
        return session_id

    def get_user_from_session_id(self, session_id: str) -> Union[User, None]:
        """getting users based on their session ids"""
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None

        return user

    def destroy_session(self, user_id: int) -> None:
        """destroying the user session"""
        try:
            self._db.update_user(user_id, session_id=None)
        except NoResultFound:
            return None
        return None

    def get_reset_password_token(self, email: str) -> str:
        """generating the password reset token"""
        user = self._db.find_user_by(email=email)
        if user:
            pass_token = _generate_uuid()
            self._db.update_user(user.id, reset_token=pass_token)
            return pass_token
        else:
            raise ValueError
