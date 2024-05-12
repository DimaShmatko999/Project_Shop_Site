import flask, flask_sqlalchemy, flask_migrate, os
import home_page, authorization_page, registration_page

shop_project = flask.Flask(import_name= "shop",template_folder= "shop_project/templates", instance_path= os.path.abspath(__file__ + "/.."))
shop_project.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
DATABASE = flask_sqlalchemy.SQLAlchemy(app = shop_project)
migrate = flask_migrate.Migrate(app= shop_project, db = DATABASE)
shop_project.register_blueprint(blueprint= home_page.home)
shop_project.register_blueprint(blueprint= authorization_page.authorization)
shop_project.register_blueprint(blueprint= registration_page.registration)
