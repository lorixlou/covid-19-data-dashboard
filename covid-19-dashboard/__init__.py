from flask import Flask

app = Flask(__name__)

from covid-19-dashboard import routes
