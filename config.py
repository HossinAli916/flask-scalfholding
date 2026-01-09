import os
from dotenv import load_dotenv
import os.path
load_dotenv()
class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'secret')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', SECRET_KEY)
    DB_PATH = os.path.join(os.path.dirname(__file__), 'database.sqlite')
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DB_PATH}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PORT = os.getenv('PORT', 5000)
