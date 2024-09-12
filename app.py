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

    query="""INSERT INTO "Unit Test 1" ("Roll Number", "Name", "Tamil Mark", "English Mark", "Maths Mark", "Science Mark", "Social Mark") VALUES ('1', 'Vignesh B', '60', '70', '70', '80', '68')"""
    InsertQuery=(f"""INSERT INTO "{table_name}" ("Roll Number", "Name", "Tamil Mark", "English Mark", "Maths Mark", "Science Mark", "Social Mark") VALUES (%s, %s, %s, %s, %s, %s, %s)""",(RollNumber,Name,TamilMark,EnglishMark,MathsMark,ScienceMark,SocialMark))
    vars=(RollNumber,Name,TamilMark,EnglishMark,MathsMark,ScienceMark,SocialMark)
    #cursor.execute("""INSERT INTO my_data (name, age, score1, score2, score3, score4, score5) VALUES (%s, %s, %s, %s, %s, %s, %s) """, (name, age, score1, score2, score3, score4, score5))
    print(query)
    cur.execute(InsertQuery)
    con.commit()

    cur.close()
    con.close()

    return render_template('Success.html')

if __name__== '__main__':
    app.run(debug=True)