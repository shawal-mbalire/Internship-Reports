from flask  import Flask, request, jsonify
from dotenv import load_dotenv
from psycopg2 import Error

import os
import psycopg2 

load_dotenv()

app = Flask(__name__)

DATABASE_NAME     = os.environ['DATABASE_NAME']
DATABASE_USER     = os.environ['DATABASE_USER']
DATABASE_PASSWORD = os.environ['DATABASE_PASSWORD']
DATABASE_HOST     = os.environ['DATABASE_HOST']
DATABASE_PORT     = os.environ['DATABASE_PORT']

connection = psycopg2.connect(
    dbname   = DATABASE_NAME,
    user     = DATABASE_USER,
    password = DATABASE_PASSWORD,
    host     = DATABASE_HOST,
    port     = DATABASE_PORT

)

cursor = connection.cursor()
cursor.execute('SELECT * FROM greenhub_trx.users;')
all = cursor.fetchall()

@app.route('/')
def home():
    return all

@app.post("/api/user")
def create_user():
    data      = request.get_json()
    phone_num = data["phone_num"]
    name      = data["name"]
    email     = data["email"]
    password  = data["password"]
    with connection:
        with connection.cursor() as cursor:
            try: 
                cursor.execute(
                    f"INSERT INTO greenhub_trx.users(phone_num, name, email, password) VALUES ('{phone_num}', '{name}', '{email}', '{password}') RETURNING phone_num;"
                )
            except Error as error:
                return {"Exception" : error.pgerror,"Code":error.pgcode}
            room_id = cursor.fetchone()[0]
    return {"id": room_id, "message": f"User {name} created."}, 201

if __name__ == '__main__':
    app.run(debug=True)