from flask  import Flask
from dotenv import load_dotenv

import os
import requests
import psycopg2 

load_dotenv()

app = Flask(__name__)

DATABASE_NAME     = os.environ['DATABASE_NAME']
DATABASE_USER     = os.environ['DATABASE_USER']
DATABASE_PASSWORD = os.environ['DATABASE_PASSWORD']
DATABASE_HOST     = os.environ['DATABASE_HOST']
DATABASE_PORT     = os.environ['DATABASE_PORT']

conn = psycopg2.connect(
    dbname   = DATABASE_NAME,
    user     = DATABASE_USER,
    password = DATABASE_PASSWORD,
    host     = DATABASE_HOST,
    port     = DATABASE_PORT

)
cursor = conn.cursor()
all = cursor.fetchall()

@app.route('/')
def hello_world():
    return all

if __name__ == '__main__':
    app.run(debug=True)