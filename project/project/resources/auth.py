import datetime
from flask import request
from flask_jwt_extended import create_access_token
from project.database.models.user import User
from flask_restful import Resource
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist
from resources.errors import SchemaValidationError, EmailAlreadyExistsError, UnauthorizedError, InternalServerError

class Signup(Resource):
    def post(self):
        try:
            email = request.form["email"]
            password = request.form["password"]
            firstname = request.form["firstname"]
            lastname = request.form["lastname"]
            user = User(email=email,password=password,firstname=firstname,lastname=lastname)
            user.hash_password()
            user.save()
            id = user.id
            return {'id': str(id)}, 200
        except FieldDoesNotExist:
            raise SchemaValidationError
        except NotUniqueError:
            raise EmailAlreadyExistsError
        except Exception:
            raise InternalServerError

class Login(Resource):
    def post(self):
        try:
            email = request.form["email"]
            password = request.form["password"]
            user = User.objects.get(email=email)
            authorized = user.check_password(password)
            if not authorized:
                raise UnauthorizedError
            expires = datetime.timedelta(days=7)
            access_token = create_access_token(identity=str(user.id), expires_delta=expires)
            return {'token': access_token}, 200
        except (UnauthorizedError, DoesNotExist):
            raise UnauthorizedError
        except Exception:
            raise InternalServerError