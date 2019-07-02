from app_config import app
from flask_graphql import GraphQLView
from schema import schema


app.add_url_rule(
        '/api',
        view_func=GraphQLView.as_view(
            'api',
            schema=schema,
            graphiql=True   # for having the GraphiQL interface
        )
    )

if __name__ == '__main__':
    app.run(port=7000, host='0.0.0.0')
