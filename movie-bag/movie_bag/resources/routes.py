from resources.movie import MoviesApi, MovieApi
from resources.user import UsersApi, UserApi 

def initialize_routes(api):
    api.add_resource(MoviesApi, '/movies')
    api.add_resource(MovieApi, '/movies/<id>')
    api.add_resource(UsersApi, '/users')
    api.add_resource(UserApi, '/users/<id>')