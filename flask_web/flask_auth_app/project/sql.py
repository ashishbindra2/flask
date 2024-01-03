from project import db, create_app, models

app = create_app()

# If db is not initialized with the app, initialize it
if not hasattr(app, 'extensions'):
    db.init_app(app)

with app.app_context():
    db.create_all()

# Additional code (if any) after creating the database tables
