from flask import Flask
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList

import flask_restful
from flask_jwt import JWT

import sys
sys.path.append("/")


from db import db


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = 'test'
    api = flask_restful.Api(app)

    jwt = JWT(app, authenticate, identity)

    api.add_resource(Item, '/item/<string:name>')
    api.add_resource(ItemList, '/items')
    api.add_resource(UserRegister, '/register')
    db.init_app(app)

    return app

if __name__ == '__main__':
    create_app().run(port=5000, debug=True)
