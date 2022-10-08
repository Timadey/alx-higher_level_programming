#!/usr/bin/python3
"""
A City Model
"""

from model_state import Base
from sqlalchemy import Column, String, Integer, ForeignKey


class City(Base):
    """
    A City that links to MySQL table 'cities'
    """
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('state.id'), nullable=False, )
