#!/usr/bin/env python3
"""
    api - module
    This module initializes the Flask application, sets up request handling and
    authorization for the API, and registers the blueprint for the application's routes.
"""

from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import CORS
import os

# Initialize the authentication mechanism based on environment variable
auth = None
auth = os.getenv('AUTH_TYPE')
if auth == 'basic_auth':
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()
elif auth == 'session_auth':
    from Session_authentication.api.v1.views.session_auth import SessionAuth
    auth = SessionAuth()
else:
    from api.v1.auth.auth import Auth
    auth = Auth()

# Create Flask application instance
app = Flask(__name__)

# Register the blueprint for API views
app.register_blueprint(app_views)

# Enable CORS for all routes under /api/v1/*
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

@app.before_request
def handle_request():
    """
    Handle requests before they reach the view functions.
    This function checks authorization for each request.
    
    It allows unauthenticated access to specific paths such as:
        - /api/v1/status/
        - /api/v1/unauthorized/
        - /api/v1/forbidden/
        - /api/v1/auth_session/login/
    
    If authorization is required and not provided, a 401 error is raised.
    If the user is not authenticated, a 403 error is raised.
    """
    handled_paths = ['/api/v1/status/',
                     '/api/v1/unauthorized/',
                     '/api/v1/forbidden/',
                     '/api/v1/auth_session/login/']
    
    if auth is not None:
        request.current_user = auth.current_user(request)
        
        # Check if authorization is required for the request path
        if auth.require_auth(request.path, handled_paths):
            # Verify that either an authorization header or session cookie is present
            if (auth.authorization_header(request) is None and
                    auth.session_cookie(request) is None):
                abort(401)  # Unauthorized
            
            # Check if the current user is authenticated
            if request.current_user is None:
                abort(403)  # Forbidden

@app.errorhandler(404)
def not_found(error) -> str:
    """
    Custom error handler for 404 Not Found errors.
    
    Returns a JSON response with an error message.
    """
    return jsonify({"error": "Not found"}), 404

@app.errorhandler(401)
def not_authorized(error) -> str:
    """
    Custom error handler for 401 Unauthorized errors.
    
    Returns a JSON response with an error message.
    """
    return jsonify({"error": "Unauthorized"}), 401

@app.errorhandler(403)
def access_forbidden(error) -> str:
    """
    Custom error handler for 403 Forbidden errors.
    
    Returns a JSON response with an error message.
    """
    return jsonify({"error": "Forbidden"}), 403

if __name__ == "__main__":
    # Run the Flask application on the specified host and port
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
