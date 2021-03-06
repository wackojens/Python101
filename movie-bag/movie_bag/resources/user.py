from flask import Response, request
from database.models.user import User
from flask_restful import Resource
from copy import deepcopy

class UsersApi(Resource):
    def get(self):
        users = User.objects().to_json()
        return Response(users, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        user = User(**body).save()
        id = user.id
        return {'id': str(id)}, 200

class UserApi(Resource):
    def get(self, id):
        users = User.objects.get(id=id).to_json()
        return Response(users, mimetype="application/json", status=200)

    def put(self, id):
        body = request.get_json()
        User.objects.get(id=id).update(**body)
        user = User.objects.get(id=id).to_json()
        return Response(user, mimetype="application/json", status=200)

    def delete(self, id):
        user = User.objects.get(id=id)
        userCopy = deepcopy(user)
        user.delete()
        return Response(userCopy.to_json(), mimetype="application/json", status=200)