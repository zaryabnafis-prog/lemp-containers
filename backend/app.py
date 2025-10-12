from flask import Flask, jsonify
import os
import mysql.connector
from datetime import datetime

app = Flask(__name__)

DB_HOST = os.getenv('DB_HOST', 'db')
DB_USER = os.getenv('DB_USER', 'appuser')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'apppass')
DB_NAME = os.getenv('DB_NAME', 'appdb')

def get_conn():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
    )

@app.get('/api/health')
def health():
    return {'status': 'ok'}

@app.get('/api')
def index():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT 'Hello from MySQL via Flask!'")
    row = cur.fetchone()
    cur.close(); conn.close()
    return jsonify(message=row[0])

@app.get('/api/time')
def server_time():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT NOW()")
    row = cur.fetchone()
    cur.close(); conn.close()
    ts = row[0]
    if isinstance(ts, datetime):
        ts = ts.isoformat(sep=' ', timespec='seconds')
    return jsonify(server_time=ts)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
