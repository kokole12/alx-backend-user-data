#!/usr/bin/env python3
"""Basic authentication implementation"""
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """basic authentication implementation class"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """function to help extract basic auth header in bytes using base64"""
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic'):
            return False

        auth_token = authorization_header.split(' ')[-1]
        return auth_token

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            item_to_decode = base64_authorization_header.encode('utf-8')
            decoded = base64.b64decode(item_to_decode)
            return decoded.decode('utf-8')
        except Exception:
            return None
