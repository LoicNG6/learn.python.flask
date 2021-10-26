from flask import wrappers
from flask.json import jsonify
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.sql.elements import Null
from sqlalchemy.sql.expression import delete, null, select, true
from sqlalchemy.sql.sqltypes import TIMESTAMP
 
MYSQL_HOST = "localhost"
MYSQL_PORT = 3306
MYSQL_USER = "root"
MYSQL_PWD = "Ab123cd456"
MYSQL_DB = "carBusiness"
 
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{}:{}@{}:{}/{}".format(MYSQL_USER,
MYSQL_PWD,
MYSQL_HOST,
MYSQL_PORT,
MYSQL_DB)

engine = create_engine(SQLALCHEMY_DATABASE_URI)

Session = sessionmaker(bind=engine)
 
session = Session()
 
base = declarative_base()

class Car(base) :
    __tablename__ = "car"

    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    brand = Column(String(255), nullable=False)
    model = Column(String(255), nullable=False)
    power = Column(Integer, nullable=False)
    isCreated = Null

    def __init__(self, brand, model, power):
        print("\n")
        print("\n")
        self.brand = brand
        self.model = model
        self.power = power
        print("Class is created")
        print("\n")
        print("\n")
        try : 
            session.add(self)
            session.commit()
            self.isCreated = True
        except Exception as exception :
            print(exception)
            self.isCreated = False

    
#car1 = Car("porshe","carrera",500)
#print((car1.brand))