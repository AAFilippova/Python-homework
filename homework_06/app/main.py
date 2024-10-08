import os
from flask import Flask
from models.models import db
from flask_migrate import Migrate
from views.views import views
from views.api import api

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
    "DATABASE_URI",
    "sqlite:///test.db",
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(views)
app.register_blueprint(api)

if __name__ == "__main__":
    app.run(debug=True)