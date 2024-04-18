from flask import Flask, render_template, request, redirect, url_for, flash
from sqlalchemy import create_engine, text

engine = create_engine("mysql+mysqlconnector://root:DjagaDjango2024.@localhost/crud")

connection = engine.connect()

app = Flask(__name__)
app.secret_key = "MY SECRET KEY"

@app.route("/")
def index():
    data = connection.execute(text("SELECT * FROM students"))
    return render_template('index.html', students=data)


@app.route("/insert", methods=['POST'])
def insert():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]

        connection.execute(text(f"INSERT INTO students (name, email, phone) VALUE ('{name}','{email}','{phone}')"))
        connection.commit()
        flash("Data Inserted Successfully")
        return redirect(url_for('index'))


@app.route("/delete/<string:id_data>", methods=["GET"])
def delete(id_data):
    connection.execute(text(f"DELETE FROM students WHERE id={id_data}"))
    connection.commit()
    flash("Data Deleted Successfully")
    return redirect(url_for('index'))


@app.route("/update", methods=['POST', 'GET'])
def update():
    if request.method == "POST":
        id_data = request.form["id"]
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]

        connection.execute(text(f"UPDATE students SET name='{name}', email='{email}', phone='{phone}' WHERE id={id_data}"))
        connection.commit()
        flash("Data Updated Successfully")

        return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)


