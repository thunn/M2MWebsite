from flask import Flask, render_template, g
#Import SQLlite for database
import sqlite3

app = Flask(__name__)

#Setup Database
app.database = "M2MWebsite/sample.db"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/team/')
def team():
    return render_template('team.html')

@app.route('/users/')
def users():
    #Create temporary connection object
    g.db = connect_db()
    #query the database
    cur = g.db.execute('select * from users')
    #Cast data to dictionary
    users = [dict(id=row[0],cardID=row[1],name=row[2],credit=row[3],bottles=row[4]) for row in cur.fetchall()]
    #Close database connection
    g.db.close()
    return render_template('users.html', users=users) #Pass variable to template

#database function
def connect_db():
    return sqlite3.connect(app.database)

#Server Config
if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=80)
#Local Config
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0')
