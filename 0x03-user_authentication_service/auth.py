#!/usr/bin/env python3
"""user authentication service to hash passwords"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """hashing the password using bcrypt"""
    encode_password = password.encode()
    return bcrypt.hashpw(encode_password, bcrypt.gensalt())
