from flask import Flask
from flask_bcrypt import Bcrypt
from flask_restful import Api
from flask_jwt_extended import JWTManager
from project.database.db import initialize_db
from project.resources.routes import initialize_routes
from project.resources.errors import errors
from project.ui.blueprintPage import blueprintPage

app = Flask(__name__)
api = Api(app, errors=errors)
bcrypt = Bcrypt(app)
app.config["JWT_SECRET_KEY"] = "t1NP63m4wnBg6nyHYKfmc2TpCOGI4nss"
jwt = JWTManager(app)

app.register_blueprint(blueprintPage)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb+srv://m001-student:m001-mongodb-basics@sandbox.4d5t5.mongodb.net/Movie-bag?retryWrites=true&w=majority'
}

initialize_db(app)
initialize_routes(api)

if __name__ == "__main__":
    app.run(debug=True, port=5000)