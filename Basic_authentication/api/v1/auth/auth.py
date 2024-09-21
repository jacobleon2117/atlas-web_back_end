# api/v1/auth/auth.py
""" 
    authentication - module
"""
from flask import request
from typing import List, TypeVar, Optional


User = TypeVar('User')


class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
            Determines if authentication is required for the given path.
        """
        if path is None:
            return True
        if not excluded_paths:
            return True

        path = path.rstrip('/')
        for excluded_path in excluded_paths:
            excluded_path = excluded_path.rstrip('/')
            if path == excluded_path:
                return False

        return True

    def authorization_header(self, request=None) -> Optional[str]:
        """
            Retrieves the authorization header from the request.
        """
        if request is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> Optional[User]:
        """
            Retrieves the current user from the request.
        """
        return None
