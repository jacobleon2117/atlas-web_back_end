#!/usr/bin/env python3
"""
SQLAlchemy model for a 'users' table.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """
    SQLAlchemy User model for 'users' table.
    """

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(255), nullable=False, unique=True)
    hashed_password = Column(String(255), nullable=False)
    session_id = Column(String(255), nullable=True)
    reset_token = Column(String(255), nullable=True)
