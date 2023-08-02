#!/use/bin/env python3
"""python script to created a filtered log"""
from typing import List
import re


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str):
    """using regex to replace occurances of certain field values"""
    for field in fields:
        message = re.sub(f'{field}=.*?{separator}',
                         f'{field}={redaction}{separator}', message)
        return message
