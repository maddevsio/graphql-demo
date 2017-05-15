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


# class CreateBook(g.relay.ClientIDMutation):
#
#     class Input:
#         book_name = g.String(required=True)
#         author_id = g.String(required=True)
#
#     book = g.Field(gqlBook)
#     author = g.Field(gqlAuthor)
#
#     @classmethod
#     def mutate_and_get_payload(cls, attr, context, info):
#         ship_name = attr.get('book_name')
#         author_id = attr.get('author_id')
#         ship = create_ship(ship_name, faction_id)
#         faction = get_faction(faction_id)
#         return IntroduceShip(ship=ship, faction=faction)
#
# class Mutator(ObjectType):
#     create_author = SQLAlchemyConnectionField(CreateAuthor)
