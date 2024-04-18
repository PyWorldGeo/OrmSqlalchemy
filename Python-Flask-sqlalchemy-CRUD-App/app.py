from flask import Flask, render_template, request, url_for, flash
from werkzeug.utils import redirect

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Student(Base):
    __tablename__ = "students"

    id = Column("id", Integer, primary_key=True)
    name = Column("name", String)
    email = Column("email", String)
    phone = Column("phone", String)

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def __repr__(self):
        return f"Student({self.id}, {self.name}, {self.email}, {self.phone})"


engine = create_engine("sqlite:///crud.db")
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

if len(session.query(Student).all()) == 0:
    student1 = Student('Giorgi Khipshidze', 'g.khipshidze@gmail.com', '+995674523')
    student2 = Student('Tamar Khergiani', 't.khergiani.com', '+995231453')
    student3 = Student('Mariam Lezhava', 'm.lezava.com', '+995678399')
    student4 = Student('Rati Mamardashvili', 'r.mamardashvili@gmail.com', '+995434315')

    session.add_all([student1, student2, student3, student4])
    session.commit()

app = Flask(__name__)
app.secret_key = 'many random bytes'



@app.route('/')
def index():
    data = session.execute(text("SELECT * FROM students"))
    return render_template('index.html', students=data)


@app.route('/insert', methods=['POST'])
def insert():
    if request.method == "POST":
        flash("Data Inserted Successfully")
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        session.execute(text(f"INSERT INTO students (name, email, phone) VALUES ('{name}', '{email}', '{phone}')"))
        session.commit()
        return redirect(url_for('index'))

@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
    flash("Record Has Been Deleted Successfully")
    session.execute(text(f"DELETE FROM students WHERE id={id_data}"))
    session.commit()
    return redirect(url_for('index'))



@app.route('/update', methods= ['POST', 'GET'])
def update():
    if request.method == 'POST':
        id_data = request.form['id']
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        session.execute(text(f"UPDATE students SET name='{name}', email='{email}', phone='{phone}' WHERE id={id_data}"))
        session.commit()
        flash("Data Updated Successfully")
        return redirect(url_for('index'))




if __name__ == "__main__":
    app.run(debug=True)
