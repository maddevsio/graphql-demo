"""SQLAlchemy db.Models."""
from graphene_sqlalchemy import SQLAlchemyObjectType
import graphene as g
from dbmodels import AuthorModel, BookModel
from graphene_sqlalchemy import SQLAlchemyConnectionField


class gqlAuthor(SQLAlchemyObjectType):
    """Authors."""

    class Meta:
        """Binding to DB model."""

        model = AuthorModel
        interfaces = (g.relay.Node, )


class gqlBook(SQLAlchemyObjectType):
    """Books."""

    class Meta:
        """Binding to DB model."""

        model = BookModel
        interfaces = (g.relay.Node, )


class Query(g.ObjectType):
    """Initializer class for all graphql root fields."""

    authors = SQLAlchemyConnectionField(gqlAuthor)
    books = SQLAlchemyConnectionField(gqlBook)
