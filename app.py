from flask import Flask, render_template,json,request
import psycopg2

app=Flask(__name__)

def connection():
    con= psycopg2.connect(database="Vignesh",host="localhost", user="postgres", password="171120",port="5432")
    return con
    
@app.route('/')
def test():
    return render_template('home.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/create',methods=['POST'])
def dbcon():
    RollNumber = request.form['Roll Number']
    Name=request.form['Name']
    TamilMark=request.form['Tamil Mark']
    EnglishMark=request.form['English Mark']
    MathsMark=request.form['Maths Mark']
    ScienceMark=request.form['Science Mark']
    SocialMark=request.form['Social Mark']
    table_name=request.form['Select Test']

    CreateQuery=f'''CREATE TABLE IF NOT EXISTS "{table_name}" (
    "Roll Number" VARCHAR(20) PRIMARY KEY,
    "Name" VARCHAR(100) NOT NULL,
    "Tamil Mark" INTEGER NOT NULL,
    "English Mark" INTEGER NOT NULL,
    "Maths Mark" INTEGER NOT NULL,
    "Science Mark" INTEGER NOT NULL,
    "Social Mark" INTEGER NOT NULL
); '''
    con=connection()
    cur=con.cursor()
    cur.execute(CreateQuery)
    con.commit()

    try:
        #INSERT INTO "Unit Test 1" ("Roll Number", "Name", "Tamil Mark", "English Mark", "Maths Mark", "Science Mark", "Social Mark") VALUES ('1', 'Vignesh B', '60', '70', '70', '80', '68')"""
        cur.execute(f"""INSERT INTO "{table_name}" ("Roll Number", "Name", "Tamil Mark", "English Mark", "Maths Mark", "Science Mark", "Social Mark") VALUES (%s, %s, %s, %s, %s, %s, %s)""",(RollNumber,Name,TamilMark,EnglishMark,MathsMark,ScienceMark,SocialMark))
        con.commit()

        cur.close()
        con.close()

        return render_template('Success.html')
    
    except Exception as e:
        print(f"Error occured : {e}")
        return render_template('error.html')

if __name__== '__main__':
    app.run(debug=True)