import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

data_file = os.path.join(os.getcwd(), __name__, '/Data/2020_travel_survey.xlsx') 

def create_app():
    app  = Flask(__name__)
    db = SQLAlchemy(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite+pysqlite:///test.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    from flask_app import routes
    app.register_blueprint(routes.bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)