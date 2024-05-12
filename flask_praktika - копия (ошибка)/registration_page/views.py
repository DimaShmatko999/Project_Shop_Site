import flask
from .models import User
from shop_project.settings import DATABASE

def show_registration_page():
    if flask.request.method == "POST":
        user = User(
            login = flask.request.form["login"],
            email = flask.request.form["email"],
            password = flask.request.form["password"],
            password_confirmation = flask.request.form["password_confirmation"]
        )
        try:
            DATABASE.session.add(user)
            DATABASE.session.commit()
        except:
            return "Error"
            
    return flask.render_template(template_name_or_list = "registration.html")