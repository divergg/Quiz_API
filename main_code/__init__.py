from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv
import psycopg2


load_dotenv()

app = Flask('TestAPI')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
url = os.getenv('DATABASE_URL')

app.config['SQLALCHEMY_DATABASE_URI'] = url

db = SQLAlchemy(app)

conn = psycopg2.connect(url)
cur = conn.cursor()

CREATE_RECORDS_TABLE = ("CREATE TABLE IF NOT EXISTS records" \
                       "(id SERIAL PRIMARY KEY, request TEXT, response TEXT, date_added_to_api TIMESTAMP, date TIMESTAMP);")

cur.execute(CREATE_RECORDS_TABLE)
conn.commit()
cur.close()
conn.close()

from . import routes


