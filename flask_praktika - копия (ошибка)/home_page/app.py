import flask

home = flask.Blueprint(
    import_name = "app",
    name = "home",
    template_folder = "home_page/templates"
)