#!/usr/bin/env python3
"""
    Route module for the API

    This module sets up the Flask application, handling various routes,
    authentication mechanisms, and error responses. It supports both
    basic and generic authentication, and integrates with CORS to
    enable cross-origin requests for specified routes.
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os

auth = None
auth = os.getenv('AUTH_TYPE')
if auth == 'basic_auth':
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()
elif auth == 'session_auth':
    from api.v1.auth.session_auth import SessionAuth
    auth = SessionAuth()
else:
    from api.v1.auth.auth import Auth
    auth = Auth()

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

@app.before_request
def before_request():
    """
    Executed before each request to handle authentication.
    
    This function checks if the request path requires authentication
    by evaluating it against a list of public routes. If authentication
    is required and not provided, the request is aborted with:
    - 401 Unauthorized: if the authorization header is missing.
    - 403 Forbidden: if the current user cannot be determined.

    The current authenticated user is set in `request.current_user`.
    """
    if auth is None:
        return
    public_routes = ['/api/v1/status/',
                     '/api/v1/unauthorized/',
                     '/api/v1/forbidden/']

    if request.path not in public_routes:
        if auth.require_auth(request.path, public_routes):
            if auth.authorization_header(request) is None:
                abort(401)
            request.current_user = auth.current_user(request)
            if request.current_user is None:
                abort(403)

@app.errorhandler(404)
def not_found(error) -> str:
    """
    Handles 404 Not Found errors.

    Returns a JSON response indicating that the requested resource
    was not found.

    Args:
        error: The error object (automatically passed in by Flask).

    Returns:
        A JSON response with an error message and a 404 status code.
    """
    return jsonify({"error": "Not found"}), 404

@app_views.route('/stats/', strict_slashes=False)
def stats() -> str:
    """
    GET /api/v1/stats

    Returns the number of users in the system.

    This route provides basic statistics about the system's usage, such as
    the number of user objects.

    Returns:
        A JSON response containing the user count.
    """
    from models.user import User
    stats = {}
    stats['users'] = User.count()
    return jsonify(stats)

@app.errorhandler(401)
def unauthorized(error) -> str:
    """
    Handles 401 Unauthorized errors.

    Returns a JSON response indicating that the request requires user
    authentication.

    Args:
        error: The error object (automatically passed in by Flask).

    Returns:
        A JSON response with an error message and a 401 status code.
    """
    return jsonify({"error": "Unauthorized"}), 401

@app.errorhandler(403)
def forbidden(error) -> str:
    """
    Handles 403 Forbidden errors.

    Returns a JSON response indicating that the server refuses to
    authorize the request, even though it understands the request.

    Args:
        error: The error object (automatically passed in by Flask).

    Returns:
        A JSON response with an error message and a 403 status code.
    """
    return jsonify({"error": "Forbidden"}), 403

if __name__ == "__main__":
    """
    Entry point for the Flask application.

    The app will run with the host and port configured through environment
    variables `API_HOST` and `API_PORT`, defaulting to `0.0.0.0` and `5000`.
    """
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
