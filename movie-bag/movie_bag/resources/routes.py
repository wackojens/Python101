from resources.movie import MoviesApi, MovieApi
from resources.user import UsersApi, UserApi
from resources.auth import SignupApi, LoginApi, LoginUi, SignupUi
from resources.reset_password import ForgotPassword, ResetPassword

def initialize_routes(api):
    api.add_resource(MoviesApi, '/movies')
    api.add_resource(MovieApi, '/movies/<id>')
    api.add_resource(UsersApi, '/users')
    api.add_resource(UserApi, '/users/<id>')
    api.add_resource(SignupApi, '/api/auth/signupApi')
    api.add_resource(SignupUi, '/api/auth/signupUi')
    api.add_resource(LoginApi, '/api/auth/loginApi')
    api.add_resource(LoginUi, '/api/auth/loginUi')
    api.add_resource(ForgotPassword, '/api/auth/forgot')
    api.add_resource(ResetPassword, '/api/auth/reset')