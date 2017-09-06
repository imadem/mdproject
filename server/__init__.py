
from flask import Flask

app = Flask(__name__, template_folder="../public", static_folder="../public", static_url_path='')

from server.routes import *