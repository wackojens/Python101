from flask import Flask
from flask_restful import Api
from database.db import initialize_db
from resources.routes import initialize_routes

app = Flask(__name__)
api = Api(app)


app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb+srv://m001-student:m001-mongodb-basics@sandbox.4d5t5.mongodb.net/Movie-bag?retryWrites=true&w=majority'
}

initialize_db(app)
initialize_routes(api)

#app.run()
if __name__ == "__main__":
    app.run(debug=True, port=5000)