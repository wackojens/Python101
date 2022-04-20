from flask import Flask
from flask_bcrypt import Bcrypt
from flask_restful import Api
from flask_mail import Mail
from database.db import initialize_db
from flask_jwt_extended import JWTManager
from resources.errors import errors
from movie_bag.ui.simplePage import simplePage
from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)

jwtKey = os.environ.get("JWT_SECRET_KEY")
app.config["JWT_SECRET_KEY"] = jwtKey

dbUser = os.environ.get("DB_USER")
dbPassword = os.environ.get("DB_PASSWORD")
dbName = os.environ.get("DB_NAME")
dbUri = os.environ.get("DB_URI")
app.config['MONGODB_SETTINGS'] = {
    'host': f'mongodb+srv://{dbUser}:{dbPassword}@{dbUri}/{dbName}?retryWrites=true&w=majority'
}

mailServer = os.environ.get("MAIL_SERVER")
mailPort = os.environ.get("MAIL_PORT")
mailUsername = os.environ.get("MAIL_USERNAME")
mailPassword = os.environ.get("MAIL_PASSWORD")

app.config["MAIL_SERVER"] = mailServer
app.config["MAIL_PORT"] = mailPort
app.config["MAIL_USERNAME"] = mailUsername
app.config["MAIL_PASSWORD"] = mailPassword

mail = Mail(app)

#imports requiring app and mail
from resources.routes import initialize_routes

api = Api(app, errors=errors)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

app.register_blueprint(simplePage, url_prefix="/ui")

initialize_db(app)
initialize_routes(api)