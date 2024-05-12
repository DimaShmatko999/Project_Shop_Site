import flask

authorization = flask.Blueprint(
    import_name = "app",
    name = "authorization",
    template_folder = "authorization_page/templates")