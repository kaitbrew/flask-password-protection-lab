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
    
class Login(Resource):
    def post(self):
        username=request.get_json()['username']
        password=request.get_json()['password']
        user=User.query.filter(User.username==username).first()

        if user and password:
            session['user_id']=user.id
            return UserSchema().dump(user),200
        return {'error':'401 Unauthorized'},401

api.add_resource(ClearSession, '/clear', endpoint='clear')
api.add_resource(Signup, '/signup')
api.add_resource(Login,'/login')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
