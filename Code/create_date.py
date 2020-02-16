from sqlalchemy.orm import sessionmaker
from faker import Faker
from db import Base,engine,User,Course

session = sessionmaker(engine)()

fake = Faker('Zh-cn')

def create_user():
	for i in range(10):
		user = user(name=fake.name(),email=fake.email())

		session.add(user)

def create_course():
	for 
