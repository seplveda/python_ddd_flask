from app import Context
from flask_sqlalchemy import SQLAlchemy

if __name__ == "__main__":
    db = SQLAlchemy()
    context = Context(db)
    context.setup()
