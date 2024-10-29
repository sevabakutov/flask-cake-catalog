from flask import Flask, render_template
from flask_migrate import Migrate
from .views import api_v1
from .models import db

app = Flask(__name__, )
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../instance/cakes_catalog.db"
app.register_blueprint(api_v1)

db.init_app(app)

migrate = Migrate(app, db)