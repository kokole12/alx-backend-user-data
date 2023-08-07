#!/usr/bin/env python3
"""auth.py file """
from flask import request
from typing import TypeVar, List


class Auth:
    """initialising a constructor for the class"""
    def __init__(self) -> None:
        pass

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """public method that returns false"""
        return False

    def authorization_header(self, request=None) -> str:
        """setting up the authorization headers"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """method to returnn the current authorised user"""
        return None
