import sqlite3
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search_result',methods=["GET"])
def display_result():
     
    date1=request.args.get("date1")
        # open the connection to the database
    conn = sqlite3.connect('trade.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from detail1 JOIN detail2 ON detail1.date=detail2.date WHERE detail1.date='1/8/2015' ")
    rows = cur.fetchall()
    conn.close()
    return render_template('output.html', rows=rows)
