from project.resources.auth import Signup, Login

def initialize_routes(api):
    api.add_resource(Signup, '/api/auth/signup')
    api.add_resource(Login, '/api/auth/login')