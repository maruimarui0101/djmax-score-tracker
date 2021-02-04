import os 
from app import create_app

from dotenv import load_dotenv

load_dotenv()

config_name = os.getenv('APP_SETTINGS') 
app = create_app(config_name)

@app.before_first_request
def create_tables():
    """Initialise creation of the database before first API request."""
    db.create_all()

if __name__ == '__main__':
    from db import db 
    db.init_app(app)
    app.run()