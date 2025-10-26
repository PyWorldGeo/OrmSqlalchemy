🧠 SQLAlchemy ORM — Relational Mapping Example

This project demonstrates how to use SQLAlchemy — Python’s most powerful ORM (Object Relational Mapper) — to manage and query relational data with Python classes instead of raw SQL.

It includes examples of one-to-many relationships, query filtering, data manipulation (CRUD), and cross-database connectivity (SQLite + MySQL).

📂 Project Structure
📦 sqlalchemy_orm_example/
│
├── app.py             # Demonstrates ORM relationships (User ↔ Address)
├── main.py            # CRUD operations, queries, and MySQL connection example
└── models.py          # ORM models, engine, session configuration

⚙️ 1️⃣ What It Does
🧩 models.py

Defines two main SQLAlchemy ORM classes:

User — represents a person with name and age

Address — represents a location tied to a user (via a foreign key)

Uses a one-to-many relationship:

User.addresses ↔ Address.user


This allows a single user to have multiple addresses.

It also sets up:

An SQLite database engine (sqlite:///)

A declarative base

A global session for database operations

💬 app.py

Demonstrates how to:

Create users and addresses

Add them to the database

Link users to multiple addresses

Update existing records

Query and print data

Example actions performed:

Create two users (Giorgi Lezava, Nino Khetaguri)

Create three addresses (Tbilisi, Batumi, etc.)

Associate users with addresses using the ORM relationship

Update an address field (city="Zestaphoni")

Print all users and addresses to the console

🧠 main.py

A detailed exploration of SQLAlchemy CRUD operations and database interaction patterns.

Includes:

Declaring Person and Thing models (one-to-one relationship)

Demonstrating add, query, filter, and delete operations

Connecting to SQLite and MySQL

Running SQL commands via text() queries

Performing conditional searches (like, in_, filter_by)

Examples of error handling, validations, and bulk operations

Example relationship mapping (User ↔ Task) and joined queries

This file effectively serves as a mini tutorial for mastering SQLAlchemy’s ORM API.

⚙️ 2️⃣ How to Run
Install Requirements
pip install sqlalchemy mysql-connector-python

Run the SQLite Example
python app.py

Run the CRUD / MySQL Demo
python main.py

🧱 Database Models Overview
Class	Table	Fields	Relationships
User	users	id, name, age	Has many Address
Address	addresses	id, city, state, zip_code, user_id	Belongs to one User
Person	persons	ssn, firstname, lastname, gender, age	Has one Thing
Thing	things	id, description, owner	Linked to Person
🧩 Example Output (from app.py)
Users:

User(id=1, name=Giorgi Lezava, address=[Address(id=2, city=Tbilisi, ...), Address(id=3, city=Batumi, ...)])
User(id=2, name=Nino Khetaguri, address=[Address(id=1, city=Zestaphoni, ...)])

Addresses:

Address(id=1, city=Zestaphoni, user_id=2, user=User(id=2, name=Nino Khetaguri))
Address(id=2, city=Tbilisi, user_id=1, user=User(id=1, name=Giorgi Lezava))
Address(id=3, city=Batumi, user_id=1, user=User(id=1, name=Giorgi Lezava))

💡 Key Concepts Demonstrated
Concept	Example
ORM (Object Relational Mapping)	Classes ↔ Tables
Relationships	relationship() and ForeignKey()
Session Management	session.add(), session.commit()
Queries	session.query().filter()
Updates	Direct object manipulation + commit
Deletes	session.delete() or .filter().delete()
Multiple Databases	SQLite + MySQL engines
Validation	@validates decorator example
Error Handling	try/except + rollback on SQLAlchemyError
🧰 Tech Stack

Python 3.10+

SQLAlchemy ORM

SQLite (default)

MySQL (optional)

mysql-connector-python

📘 Learning Goals

This project is designed to help you:

Understand SQLAlchemy’s Declarative ORM syntax

Manage relationships between models

Perform CRUD operations efficiently

Write queries using SQLAlchemy’s Pythonic API

Integrate Python applications with relational databases

🧾 License

MIT License — free to use, modify, and distribute.
