#!/usr/bin/env python3
"""
    Python script to has password using the bycrypt module
    func: def hash_password
    Args:
        password: str
    returns string of hashed password
"""


import bcrypt


def hash_password(password: str) -> str:
    """hashing the password using bycrypt"""
    encoded_password = password.encode()
    hashed = bcrypt.hashpw(encoded_password, bcrypt.gensalt())
    return hashed
