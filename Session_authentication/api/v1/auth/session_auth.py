#!/usr/bin/env python3
"""Session Authorization Module
"""
from flask import request
from api.v1.auth.auth import Auth
from models.user import User
import os
import uuid


class SessionAuth(Auth):
    """
        session Authorization Class
    """

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Create a session ID for a user.

        Args:
            user_id (str): The ID of the user for whom to create the session.

        Returns:
            str: The generated session ID, or None if the user_id is invalid.
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Retrieve the user ID associated with a given session ID.

        Args:
            session_id (str): The session ID to look up.

        Returns:
            str: The associated user ID, or None if the session ID is invalid.
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """Return the currently authenticated user.

        Args:
            request: The Flask request object.

        Returns:
            User: The user object corresponding to the current session, or None if not authenticated.
        """
        session_cookie = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_cookie)
        return User.get(user_id)

    def destroy_session(self, request=None) -> bool:
        """Remove a user's session.

        Args:
            request: The Flask request object.

        Returns:
            bool: True if the session was successfully destroyed, False otherwise.
        """
        if request is None:
            return False
        cookie = self.session_cookie(request)
        if cookie is None or self.user_id_for_session_id(cookie) is None:
            return False
        del self.user_id_by_session_id[cookie]
        return True
