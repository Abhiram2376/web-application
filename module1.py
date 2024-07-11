from flask import *
import sqlite3

app = Flask(__name__,static_folder='static',static_url_path='/src')

app.config['TEMPLATES_AUTO_RELOAD']=True

@app.route("/",methods=['POST','GET'])
def main():
    if request.method=='POST':
        conn=sqlite3.connect("users.db")
        cursor=conn.cursor()
        name=request.form.get("name")
        email=request.form.get("email")
        age=request.form.get("age")
        dob=request.form.get("dob")
        cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS users(
            uid INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            age INTEGER,
            dob TEXT
        )""")
        cursor.execute(f"INSERT INTO users VALUES(null,?,?,?,?)",(name,email,age,dob))
        conn.commit()
        conn.close()
        return redirect('/users')
    conn=sqlite3.connect("users.db")
    cursor=conn.cursor()
    cursor.execute(f"""
    CREATE TABLE IF NOT EXISTS users(
        uid INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        age INTEGER,
        dob TEXT
    )""")
    conn.commit()
    conn.close()
    return render_template('index.html')

@app.route('/users')
def users():
    
    conn=sqlite3.connect("users.db")
    cursor=conn.cursor()
    cursor.execute(f"""
    CREATE TABLE IF NOT EXISTS users(
        uid INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        age INTEGER,
        dob TEXT
    )""")
    cursor.execute("SELECT name,email,age,dob FROM users")
    data=cursor.fetchall()
    # conn.commit()
    conn.close()

    return render_template('users.html',data=data)

app.run(debug=True)
