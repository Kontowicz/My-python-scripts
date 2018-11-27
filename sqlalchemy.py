from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, ForeignKey, String, MetaData, select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine("sqlite:///users.db")
Base = declarative_base()
Session = sessionmaker(bind=engine)
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

#Database creation
class User(Base):
	__tablename__ = 'user'
	
	id = Column(Integer, primary_key = True, autoincrement=True)
	
	name = Column(String)
	surname = Column(String)
	
class Adress(Base):
	__tablename__ = 'adres'
	
	id = Column(Integer, primary_key = True, autoincrement=True)
	id_osoba = Column(Integer, ForeignKey('user.id'))
	
	street = Column(String)
	city = Column(String)
	postalCode = Column(String)
	
class Telephone(Base):
	__tablename__ = 'telephone'
	
	id = Column(Integer, primary_key = True, autoincrement=True)
	id_osoba = Column(Integer, ForeignKey('user.id'))
	
	number = Column(String)
	
class PersonList(Base):
	__tablename__ = 'personList'
	
	id = Column(Integer, primary_key = True, autoincrement=True)
	id_osoba = Column(Integer, ForeignKey('user.id'))
	
	name = Column(String)
	
class Email(Base):
	__tablename__ = 'email'
	
	id = Column(Integer, primary_key = True, autoincrement=True)
	id_osoba = Column(Integer, ForeignKey('user.id'))
	
	email = Column(String)

Base.metadata.create_all(engine)
meta = MetaData(engine, reflect=True)
meta.create_all()
conn = engine.connect()

def print_all(Meta, Conn):
	tablenames = ['user', 'adres', 'telephone', 'personList', 'email']
	for table  in tablenames:
		tab = Meta.tables[table]
		s = select([tab])
		res = Conn.execute(s)
		print(table)
		for r in res:
			print(r)
		
def add_user(Name, Surname, Meta, Conn):
	table = Meta.tables['user']
	Conn.execute(table.insert(),[{'name':Name,'surname':Surname}])
	s = select([table])
	res = Conn.execute(s)
	id = 0
	for r in res:
		id = r['id']
	return id
	
def add_adr(Street, City, PostalCode, Id, Meta, Conn):
	table = Meta.tables['adres']
	Conn.execute(table.insert(),[{'street':Street,'city':City, 'postalCode':PostalCode, 'id_osoba': Id}])
	
def add_telephone(Number, Id, Meta, Conn):
	table = Meta.tables['telephone']
	Conn.execute(table.insert(),[{'number':Number, 'id_osoba': Id}])
	
def add_personList(Name, Id, Meta, Conn):
	table = Meta.tables['personList']
	Conn.execute(table.insert(),[{'name':Name, 'id_osoba': Id}])	
	
def add_email(Mail, Id, Meta, Conn):
	table = Meta.tables['email']
	Conn.execute(table.insert(),[{'email':Mail, 'id_osoba': Id}])

def add_to_all(Name, Surname, Street, City, PostalCode, Number, Person, Mail, Meta, Conn):
	id = add_user(Name, Surname, Meta, Conn)
	add_adr(Street, City, PostalCode, id, Meta, Conn)
	add_telephone(Number, id, Meta, Conn)
	add_personList(Person, id, Meta, Conn)
	add_email(Mail, id, Meta, Conn)

	
def find(Name, Meta, Conn):
	table = Meta.tables['user']
	select_st = table.select().where(
	table.c.name == Name)
	res = Conn.execute(select_st)
	for _row in res:
		print(_row)
	
	for _row in res:
		return(_row['id'])
	
		
	
while True:
	print('1. Show all tables')
	print('2. Find')
	print('3. Add user')
	print('4 Add person')
	print('5 Add adress')
	case = input()
	if case == '1':
		print_all(meta, conn)
	elif case == '2':
		print('Enter person name:')
		name = input()
		find(name, meta, conn)
	elif case == '3':
		print('Enter: Name, Surname, Street, City, PostalCode, Number, Person, Mail')
		data = []
		for i in range(0, 8):
			tmp = input()
			data.append(tmp)
		add_to_all(data[0], data[1], data[2], data[3], data[4], data[5], data[6],  data[7], meta, conn)
	elif case == '4':
		print('Enter user name:')
		Name = input()
		table = meta.tables['user']
		select_st = table.select().where(
		table.c.name == Name)
		res = conn.execute(select_st)
		id = 0
		for _row in res:
			id = _row['id']
			
		print('Enter friend name')
		fn = input()
		add_personList(fn, id, meta, conn)
	elif case == '5':
		print('Enter user name:')
		Name = input()
		table = meta.tables['user']
		select_st = table.select().where(
		table.c.name == Name)
		res = conn.execute(select_st)
		id = 0
		for _row in res:
			id = _row['id']
		
		print('Enter: street, city, postal code')
		street = input()
		city = input()
		poco = input()
		
		add_adr(street, city, poco, id, meta, conn)
	
