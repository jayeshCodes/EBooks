"""imports"""
import os

from dotenv import load_dotenv

load_dotenv()

db_name = os.getenv("DB")
host = os.getenv("HOST")
password = os.getenv("PASSWORD")
user = os.getenv("USER")
port = os.getenv("PORT")
db_url = os.getenv("DB_URL")
