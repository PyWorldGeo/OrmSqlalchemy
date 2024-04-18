from models import Address, User, session

user1 = User(name="Giorgi Lezava", age=23)
user2 = User(name="Nino Khetaguri", age=25)

session.add_all([user1, user2])

address1 = Address(city="Tbilisi", state="Saburtalo", zip_code="0165")
address2 = Address(city="Tbilisi", state="Vake", zip_code="0156")
address3 = Address(city="Batumi", state="Batumi Bulevard", zip_code="0681")

session.add_all([address1, address2, address3])

session.commit()


user1.addresses.extend([address3, address2])
user2.addresses.append(address1)
session.commit()

print(user1.addresses)
