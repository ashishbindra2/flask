from app.extensions import db
from app.extensions import User

def print_users():
    # Retrieve all users from the database
    all_users = User.query.all()

    # Print the users to the terminal
    for user in all_users:
        print(f'User ID: {user.id}, Email: {user.email}, Name: {user.name}')

P
if __name__ == "__main__":
    # Run the script if executed directly
    print_users()
