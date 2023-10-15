#!/usr/bin/env python3
"""
DB Storage engine
"""
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base import BaseModel, Base

class DBStorage():
    """
    DbStorage class
    """
    __session = None
    __engine = None

    def __init__(self, *args, **kwargs):
        """
        initialization
        """
        db = getenv("SAVY_DB", "savy_db")
        user = getenv("SAVY_USER", "savy_user")
        host = getenv("SAVY_HOST", "localhost")
        pwd = getenv("SAVY_PWD", "Savy-2146")

        url = f"mysql+mysqlconnector://{user}:{pwd}@{host}/{db}"
        self.__engine = create_engine(url)

    def reload(self):
        """
        creates a new session
        """
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session)

    def save(self, obj):
        """
        adds an obj to the session
        then saves it to the database
        """
        self.__session.add(obj)
        self.__session.commit()