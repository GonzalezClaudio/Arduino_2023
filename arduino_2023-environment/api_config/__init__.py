from flask import (
    Flask,
)
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


app = Flask('MyApp')
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:claudio0802@localhost/postgres"  # noqa
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)