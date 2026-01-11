#!/usr/bin/env python3

from flask import request, session
from flask_restful import Resource

from config import app, db, api
from models import User, UserSchema

class Signup(Resource):
    def post(self):
        json=request.get_json()
        user=User(username=json['username'])
        db.session.add(user)
        db.session.commit()
        return UserSchema().dump(user),201

class ClearSession(Resource):

    def delete(self):
    
        session['page_views'] = None
        session['user_id'] = None

        return {}, 204

api.add_resource(ClearSession, '/clear', endpoint='clear')
api.add_resource(Signup, '/signup')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
