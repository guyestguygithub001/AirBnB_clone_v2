#!/usr/bin/python3
""" new class model for the sqlAlchemy. """

from sqlalchemy.orm import sessionmaker, relationship, scoped_session
from sqlalchemy import (create_engine)
from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.state import State
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.city import City

class DBStorage:
    """Makes tables in environmental."""
    __engine = None
    __session = None

    def __init__(self):
        """Makes engine."""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """Method for queries on currect database session."""
        objects_dictionary = {}

        if cls is None:
            objects_list = self.__session.query(State).all()
            objects_list.extend(self.__session.query(City).all())
            objects_list.extend(self.__session.query(User).all())
            objects_list.extend(self.__session.query(Place).all())
            objects_list.extend(self.__session.query(Review).all())
            objects_list.extend(self.__session.query(Amenity).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            objects_list = self.__session.query(cls).all()

        for obj in objects_list:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            objects_dictionary[key] = obj

        return objects_dictionary

    def save(self):
        """save effected changes.
        """
        self.__session.commit()

    def new(self, obj):
        """adds new element to table.
        """
        self.__session.add(obj)

    def delete(self, obj=None):
        """clears an element in table.
        """
        if obj:
            self.session.delete(obj)

    def close(self):
        """  removes calls.()
        """
        self.__session.close()

    def reload(self):
        """configuration
        """
        Base.metadata.create_all(self.__engine)
        sec = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sec)
        self.__session = Session()

