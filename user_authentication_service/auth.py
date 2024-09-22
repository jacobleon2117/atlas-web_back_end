#!/usr/bin/env python3
"""
    auth module
"""

import bcrypt
import uuid
from db import DB
from user import User
from sqlalchemy.exc import NoResultFound


class Auth:
    """
        Auth class - database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
            new user
        """

        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed = _hash_password(password)
            return self._db.add_user(email, hashed)

    def valid_login(self, email: str, password: str) -> bool:
        """
            login attempt
        """
        try:
            user = self._db.find_user_by(email=email)
            checked_pw = password.encode('utf-8')
            hashed_pw = user.hashed_password
            return bcrypt.checkpw(checked_pw, hashed_pw)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """
            session ID
        """

        try:
            user = self._db.find_user_by(email=email)
            new_session = _generate_uuid()
            self._db.update_user(user.id, session_id=new_session)
            session_user = self._db.find_user_by(session_id=new_session)
            return session_user.session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """
            retrieve session id
        """

        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """
            destroy user session
        """

        self._db.update_user(user_id, session_id=None)

    def get_reset_password_token(self, email: str) -> str:
        """
            password reset token
        """
        try:
            user = self._db.find_user_by(email=email)
            reset = _generate_uuid()
            self._db.update_user(user.id, reset_token=reset)
            return reset
        except NoResultFound:
            raise ValueError

    def update_password(self, reset_token: str, password: str) -> None:
        """
            reset method
        """
        try:
            u = self._db.find_user_by(reset_token=reset_token)
            pw = _hash_password(password)
            self._db.update_user(u.id, hashed_password=pw, reset_token=None)
        except NoResultFound:
            raise ValueError


def _hash_password(password: str) -> bytes:
    """
        password string
    """

    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """
        new UUID
    """

    return str(uuid.uuid4())
