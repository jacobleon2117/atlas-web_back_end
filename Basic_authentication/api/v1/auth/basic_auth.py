# api/v1/auth/basic_auth.py
"""
    Basic authorization - module
"""
from typing import TypeVar, Tuple
import base64
from models.user import User
from api.v1.auth.auth import Auth

User = TypeVar('User', bound=User)


class BasicAuth(Auth):
    """
        BasicAuth class inheriting from Auth.
    """
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """
            Extracts the Base64 part of the Authorization header.
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header.split("Basic ")[1]

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """
            Decodes a Base64 encoded string.
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except (base64.binascii.Error, UnicodeDecodeError):
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> Tuple[str, str]:
        """
            Extracts the user email and password from the decoded Base64 string.
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        return tuple(decoded_base64_authorization_header.split(':', 1))

    def user_object_from_credentials(self, user_email: str, user_pwd: str) -> User:
        """
            Returns the User instance based on email and password.
        """
        if not isinstance(user_email, str) or user_email is None:
            return None
        if not isinstance(user_pwd, str) or user_pwd is None:
            return None

        users = User.search(user_email)
        if not users:
            return None

        for user in users:
            if user.is_valid_password(user_pwd):
                return user

        return None

    def current_user(self, request=None) -> User:
        """
            Retrieves the User instance for a request.
        """
        if request is None:
            return None

        auth_header = self.authorization_header(request)
        if auth_header is None:
            return None

        base64_auth_header = self.extract_base64_authorization_header(auth_header)
        if base64_auth_header is None:
            return None

        decoded_auth_header = self.decode_base64_authorization_header(base64_auth_header)
        if decoded_auth_header is None:
            return None

        user_email, user_pwd = self.extract_user_credentials(decoded_auth_header)
        if user_email is None or user_pwd is None:
            return None

        return self.user_object_from_credentials(user_email, user_pwd)
