"""
Database Management
===================

This module provides some helper functions to manage database connections
and sessions.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = None
session_factory = sessionmaker()
Session = scoped_session(session_factory)  # TODO: define session scope

ModelBase = declarative_base()


def initialize_db(connection_string):
    """
    Connect to the database specified by the connection string

    :param connection_string: A string specifying the database details. The
    format of this string can be found in the SQLAlchemy documentation.
    :type connection_string: str
    """

    global engine

    engine = create_engine(connection_string)
    Session.configure(bind=engine)


def create_tables():
    """Create all corresponding database tables subclassing from `ModelBase`."""
    ModelBase.metadata.create_all(engine)
