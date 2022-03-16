from app import create_app,db
from app.models import User


# Creating app instance
app = create_app()


if __name__ == '__main__':
    app.run() 