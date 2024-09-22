#!/usr/bin/env python3
"""
    auth - module
"""
from flask import request
from typing import List, TypeVar, Optional
import os

User = TypeVar('User')


class Auth():
    """
        Auth class
    """
    
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
            auth requirement
        """
        if path is not None and excluded_paths is not None:
            for route in excluded_paths:
                if path == route or path + "/" == route:
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """
            auth header
        """
        if request is None:
            return None
        else:
            if 'Authorization' not in request.headers:
                return None
            else:
                return request.headers['Authorization']

    def current_user(self, request=None) -> Optional[User]:
        """
            current user object
        """
        return None

    def session_cookie(self, request=None):
        """
            returns the cookies
        """

        if request is None:
            return None
        cookie = request.cookies.get(os.getenv('SESSION_NAME'))
        return cookie
