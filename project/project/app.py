import os
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_restful import Api
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
from project.database.db import initialize_db
from project.resources.routes import initialize_routes
from project.resources.errors import errors
from project.ui.blueprintPage import blueprintPage

load_dotenv()

app = Flask(__name__)
api = Api(app, errors=errors)
bcrypt = Bcrypt(app)
jwt_key = os.environ.get("JWT_SECRET_KEY")
app.config["JWT_SECRET_KEY"] = jwt_key
jwt = JWTManager(app)
app.register_blueprint(blueprintPage)
user = os.environ.get("DB_USER")
password = os.environ.get("DB_PASSWORD")
db_name = os.environ.get("DB_NAME")
db_uri = os.environ.get("DB_URI")
app.config['MONGODB_SETTINGS'] = {
    'host': f'mongodb+srv://{user}:{password}@{db_uri}/{db_name}?retryWrites=true&w=majority'
}

initialize_db(app)
initialize_routes(api)

if __name__ == "__main__":
    app.run(debug=True, port=5000)