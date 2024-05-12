import home_page, authorization_page, registration_page
from .settings import shop_project

home_page.home.add_url_rule(rule= "/", view_func= home_page.show_home_page, method= ["GET", "POST"])
shop_project.register_blueprint(blueprint= registration_page.registration)

registration_page.registration.add_url_rule(rule= "/registration/", view_func= registration_page.show_registration_page)
authorization_page.authorization.add_url_rule(rule= "/authorization/", view_func= authorization_page.show_authorization_page)