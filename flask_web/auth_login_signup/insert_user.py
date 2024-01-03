from app.extensions import User
from app.extensions import db


def insert_user(email, password, name):
    # Create a new User instance
    new_user = User(email=email, password=password, name=name)

    # Add the new user to the database session
    db.session.add(new_user)

    # Commit the changes to the database
    db.session.commit()


if __name__ == "__main__":
    # Run the script if executed directly
    # Example usage:
    insert_user(email="ashi@example.com", password="ashi", name="John Doe")
