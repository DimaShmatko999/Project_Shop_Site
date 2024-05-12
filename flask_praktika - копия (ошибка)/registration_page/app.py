import flask

registration = flask.Blueprint(
    import_name = "app",
    name = "registration",
    template_folder = "registration_page/templates"
)