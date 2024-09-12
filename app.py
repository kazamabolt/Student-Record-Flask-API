from flask import Flask, render_template
import psycopg2

app=Flask(__name__)

def connection():
    con= psycopg2.connect(database="Vignesh",host="localhost", user="postgres", password="171120",port="5432")
    return con
    
@app.route('/')
def test():
    return render_template('login.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/create',methods=['POST'])
def dbcon():
    query=f'''CREATE TABLE IF NOT EXISTS "{table_name}" (RollNumber VARCHAR(255),Name VARCHAR(255), Year INT); '''
    con=connection()
    cur=con.cursor()
    cur.execute(query)
    con.commit()
    cur.close()
    con.close()

    return "Successful"

if __name__== '__main__':
    app.run(debug=True)