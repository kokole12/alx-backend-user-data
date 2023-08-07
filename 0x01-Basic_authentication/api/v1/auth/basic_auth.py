#!/usr/bin/env python3
"""Basic authentication implementation"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """basic authentication implementation class"""

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """function to help extract basic auth header in bytes using base64"""
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic'):
            return False

        auth_token = authorization_header.split(' ')[-1]
        return auth_token
