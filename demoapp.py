"""GraphQL demo app."""
from flask import Flask
from flask_graphql import GraphQLView
import graphene as g

################################################
app = Flask(__name__)
with app.app_context():
    app.config.from_object('config.main-config.DevConfig')
    from gqlmodels import Query
    import dbmodels as mdb

mdb.db.init_app(app)

graphView = GraphQLView.as_view(
    'graphql',
    schema=g.Schema(
        query=Query,
        # mutation=Mutator,
    ),
    # middleware=[AuthMiddleware()],
    graphiql=True
)

# Main app route
app.add_url_rule('/', view_func=graphView)


def initDbView():
    """Here we init db and pass initial data."""
    mdb.db.reflect()
    mdb.db.drop_all()
    mdb.db.create_all()

    dbAuthor1 = mdb.AuthorModel(
        first_name="Leo", last_name="Tolstoi"
    )
    dbBook1 = mdb.BookModel(
        name="Anna Karenina", author=dbAuthor1
    )
    dbBook2 = mdb.BookModel(
        name="War and Peace", author=dbAuthor1
    )
    dbAuthor2 = mdb.AuthorModel(
        first_name="Gabriel", last_name="Garcia Markez"
    )
    dbBook3 = mdb.BookModel(
        name="One Hundred Years of Solitude", author=dbAuthor2
    )
    dbBook4 = mdb.BookModel(
        name="No One Writes to the Colonel", author=dbAuthor2
    )

    mdb.db_session.add(dbAuthor1)
    mdb.db_session.add(dbBook1)
    mdb.db_session.add(dbBook2)
    mdb.db_session.add(dbAuthor2)
    mdb.db_session.add(dbBook3)
    mdb.db_session.add(dbBook4)

    mdb.db_session.commit()
    return "DB reset"


# DB init route
app.add_url_rule('/initdb', view_func=initDbView)
