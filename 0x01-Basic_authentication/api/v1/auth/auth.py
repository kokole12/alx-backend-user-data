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
        if path is None:
            return True
        if excluded_paths == [] or excluded_paths is None:
            return True
        if path in excluded_paths:
            return False

        for excluded_path in excluded_paths:
            if excluded_path.startswith(path):
                return False
            elif path.startswith(excluded_path):
                return False
            elif excluded_path[-1] == "*":
                if path.startswith(excluded_path[:-1]):
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """setting up the authorization headers"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """method to returnn the current authorised user"""
        return None
