from flask import Flask
from flask import render_template
import sqlite3

conn=sqlite3.connect("../skripsi/usersdatabase4.db", check_same_thread=False)
c=conn.cursor()

app=Flask(__name__)

@app.route("/")
def index():
    c.execute("SELECT * FROM users")
    return render_template('index.html', rows = c.fetchall(), zip=zip)

@app.route("/absensi")
def absensi():
    c.execute("select absensi.id, name, jabatan, temp, date from absensi inner join users on absensi.users_id = users.id")
    result = c.fetchall()
    return render_template('absensi.html', results=result, zip=zip)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
