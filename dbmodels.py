"""SQLAlchemy db.Models."""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask import current_app as app
db = SQLAlchemy()

engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
db_session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


# class AuthorModel(Base):
class AuthorModel(db.Model, Base):
    """Authors."""

    # This class, as well as BookModel class can be inherited just from Base
    # It would be enough for mapping to work
    # We need db.Model here just for db.create_all() which is used to reset db

    __tablename__ = 'authors'

    id = db.Column(
        db.Integer,
        primary_key=True,
        nullable=False,
        autoincrement=True
    )
    first_name = db.Column(db.String(200))
    last_name = db.Column(db.String(200))

    def __init__(self, first_name=None, last_name=None):
        """DB model constructor."""
        self.first_name = first_name
        self.last_name = last_name


# class BookModel(Base):
class BookModel(db.Model, Base):
    """Books."""

    __tablename__ = 'books'

    id = db.Column(
        db.Integer,
        primary_key=True,
        nullable=False,
        autoincrement=True
    )
    name = db.Column(db.String(200))
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))
    author = db.relationship("AuthorModel", backref="books")

    def __init__(self, name=None, author=None):
        """DB model constructor."""
        self.name = name
        self.author = author
