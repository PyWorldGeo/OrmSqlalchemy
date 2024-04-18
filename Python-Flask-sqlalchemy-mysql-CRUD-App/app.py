from flask import Flask, render_template, request, url_for, flash
from werkzeug.utils import redirect

from sqlalchemy import create_engine, text




engine = create_engine("mysql+mysqlconnector://root:DjagaDjango2024.@localhost/crud")

# Test the connection
connection = engine.connect()


app = Flask(__name__)
app.secret_key = 'many random bytes'



@app.route('/')
def index():
    data = connection.execute(text("SELECT * FROM students"))
    return render_template('index.html', students=data)


@app.route('/insert', methods=['POST'])
def insert():
    if request.method == "POST":
        flash("Data Inserted Successfully")
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        connection.execute(text(f"INSERT INTO students (name, email, phone) VALUES ('{name}', '{email}', '{phone}')"))
        connection.commit()
        return redirect(url_for('index'))

@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
    flash("Record Has Been Deleted Successfully")
    connection.execute(text(f"DELETE FROM students WHERE id={id_data}"))
    connection.commit()
    return redirect(url_for('index'))



@app.route('/update', methods= ['POST', 'GET'])
def update():
    if request.method == 'POST':
        id_data = request.form['id']
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        connection.execute(text(f"UPDATE students SET name='{name}', email='{email}', phone='{phone}' WHERE id={id_data}"))
        connection.commit()
        flash("Data Updated Successfully")
        return redirect(url_for('index'))




if __name__ == "__main__":
    app.run(debug=True)
