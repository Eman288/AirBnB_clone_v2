#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    name = Column(String(128, collation='latin1_swedish_ci'), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    __tablename__ = "cities"
