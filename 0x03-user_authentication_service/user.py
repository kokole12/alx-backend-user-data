#!/usr/bin/env python3
"""
    implementing a sqlalchemy model to create the table users
"""


from sqlalchemy import String, Integer, Column
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    """implementing the table"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_passsword = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
