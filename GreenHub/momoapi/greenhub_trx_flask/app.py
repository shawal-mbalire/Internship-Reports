from flask import Flask

import os
import psycopg2 
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL)

@app.route('/')
def hello_world():
    return 'Hello, World!'