from flask import Flask
from flask_cors import CORS
from backend.model.usuario import Usuario


app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return "<p>Servidor flask funcionando</p>"