# should only be concerned about creating the application itself

from flask import Flask, request, jsonify, abort
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)


from books import books
app.register_blueprint(books)



