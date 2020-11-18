# should only be concerned about creating the application itself

from flask import Flask, request, jsonify, abort
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)


from controllers import registerable_controllers

for controller in registerable_controllers:
    app.register_blueprint(controller)
