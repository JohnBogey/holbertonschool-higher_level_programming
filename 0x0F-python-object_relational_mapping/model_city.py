#!/usr/bin/python3
'''class definition of City and instance of Base'''
import sys
from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    '''City class inherits from Base'''
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128))
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
