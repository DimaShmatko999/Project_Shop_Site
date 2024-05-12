from shop_project.settings import DATABASE

class User(DATABASE.Model):
    id = DATABASE.Column(DATABASE.Integer, primary_key = True),
    email = DATABASE.Column(DATABASE.String(30), nullable = False),
    login = DATABASE.Column(DATABASE.String(75), nullable = False),
    password = DATABASE.Column(DATABASE.String(25), nullable = False)
    
    def __repr__(self) -> str:
        return f"id: {self.id}"