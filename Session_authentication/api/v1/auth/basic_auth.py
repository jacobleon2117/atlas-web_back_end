#!/usr/bin/env python3
""" Module of auth methods
"""
from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.base import Base
from models.user import User


class BasicAuth(Auth):
    """ BasicAuth class
        Contains methods for authenticating users
    """

    def extract_base64_authorization_header(self, auth_header: str) -> str:
        """ Extract an authorization header
        """
        if auth_header is None or type(auth_header) is not str:
            return None
        if auth_header.split(" ")[0] != 'Basic':
            return None
        return auth_header.split(" ")[1]

    def decode_base64_authorization_header(self, auth_header_64: str) -> str:
        """ decode base64 string
        """
        if auth_header_64 is None or type(auth_header_64) is not str:
            return None
        try:
            result = base64.b64decode(auth_header_64).decode('utf-8')
        except (base64.binascii.Error, UnicodeDecodeError):
            result = None
        return result

    def extract_user_credentials(self, decoded_header: str) -> (str, str):
        """ return user info extracted from decoded header
        """

        if (decoded_header is None or
                type(decoded_header) is not str or
                ':' not in decoded_header):
            return (None, None)
        extracted = decoded_header.split(':')
        return (extracted[0], extracted[1])

    def user_object_from_credentials(self, e: str, pw: str) -> TypeVar('User'):
        """ retrieve a user from storage based on provided
            credentials
            e: user email
            pw: user password
        """
        if e is None or type(e) is not str:
            return None
        if pw is None or type(pw) is not str:
            return None
        try:
            user_list = User.search({'email': e})
            if len(user_list) == 0:
                return None
            if not user_list[0].is_valid_password(pw):
                return None
            return user_list[0]
        except KeyError:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ retrieve User instance for request
        """
        header = self.authorization_header(request)
        b64header = self.extract_base64_authorization_header(header)
        decoded_header = self.decode_base64_authorization_header(b64header)
        info = self.extract_user_credentials(decoded_header)
        user_object = self.user_object_from_credentials(info[0], info[1])
        return user_object
