from sqlalchemy import create_engine, not_, and_, or_, func
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base
from random import choice

Base = declarative_base()

class Person(Base):
    __tablename__ = "persons"

    id = Column("id", Integer, primary_key=True)
    name = Column("name", String)
    age = Column("age", Integer)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(id={self.id}, name={self.name}, age={self.age})"


engine = create_engine("sqlite:///:memory:")

Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)

session = Session()

names = ["Levani", "Mariami", "Daviti", "Elene", "Giorgi"]
ages = [22, 16, 45, 33, 20, 55]



# for i in range(20):
#     person = Person(name=choice(names), age=choice(ages))
#     session.add(person)
#     session.commit()
#
# all_persons = session.query(Person).all()
# print(all_persons)

people = []
for i in range(20):
    person = Person(name=choice(names), age=choice(ages))
    people.append(person)


session.add_all(people)
session.commit()
#
#
# all_persons = session.query(Person).all()
# for info in all_persons:
#     print(info)

persons = session.query(Person).all()[0]
print(persons)
persons.name = "Elizabet"
session.commit()
persons = session.query(Person).all()[0]
print(persons)

# session.delete(all_persons)
# session.commit()



# all_persons = session.query(Person).filter_by(age=20, name="Elene").all()
# print(all_persons)

# all_persons = session.query(Person).filter_by(age=20, name="Elene").one_or_none()
# print(all_persons)

# all_persons = session.query(Person).filter_by(age=20, name="Elene").first()
# print(all_persons)


# all_persons = session.query(Person).filter(Person.age>20).all()
# print(all_persons)


# all_persons = session.query(Person).where((Person.age > 20) | (Person.name=="Elene")).all()
# print(all_persons)

# all_persons = session.query(Person).where(not_(Person.age > 20) | (Person.name=="Elene")).all()
# print(all_persons)

# all_persons = session.query(Person).filter(Person.name.in_(["Mariami", "Levani"])).all()
# print(all_persons)


# all_persons = session.query(Person).order_by(Person.age).all()
# print(all_persons)

# all_persons = session.query(Person).order_by(Person.name).all()
# print(all_persons)

# people = session.query(Person.age, func.count(Person.id)).group_by(Person.age).all()
# print(people)