import os
from flask import Flask, render_template
# from flask_app.models import db, migrate

data_file = os.path.join(os.getcwd(), __name__, '/Data/2020_travel_survey.xlsx') 

def create_app():
    app  = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite+pysqlite:///test.db"

    # db.init_app(app)
    # migrate.init_app(app, db)

    from flask_app.routes import main_routes
    app.register_blueprint(main_routes.bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)