#!/usr/bin/env python3
"""
    authentication - module
"""
from flask import request
from typing import List, TypeVar, Optional

User = TypeVar('User')


class Auth:
    """
    Base class for managing authentication in the API.

    This class provides methods to determine if authentication is
    required for specific paths, retrieve the authorization header,
    and obtain the current user based on the request.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if authentication is required for the given path.

        Args:
            path (str): The requested API endpoint.
            excluded_paths (List[str]): List of endpoints that do not require authentication.

        Returns:
            bool: True if authentication is required, False otherwise.
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

        Args:
            request: The incoming request object.

        Returns:
            Optional[str]: The value of the 'Authorization' header, or None if it does not exist.
        """
        if request is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> Optional[User]:
        """
        Retrieves the current user from the request.

        Args:
            request: The incoming request object.

        Returns:
            Optional[User]: An instance of the user if authenticated, or None if not.
        """
        return None
