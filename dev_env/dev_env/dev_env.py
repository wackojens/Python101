from dotenv import load_dotenv
load_dotenv()

import os

api = os.environ.get("API_KEY")
uri = os.environ["DB_URI"]
port = os.environ.get("DB_PORT")
user = os.environ["DB_USER"]
password = os.environ.get("DB_PASSWORD")
msg = os.environ["HELLO_MSG"]

print(api)
print(uri)
print(port)
print(user)
print(password)
print(msg)