from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import sessionmaker
 
dbExists = false
engine = create_engine('mysql://root:root@localhost:3306/assign1', echo=False)
try:
    engine.connect()
    dbExists = true
except: 
    engine = create_engine('mysql://root:root@localhost:3306')
    engine.execute("CREATE DATABASE IF NOT EXISTS assign1")
    
engine.execute("USE assign1")
Base = declarative_base()
 
class Expense(Base):
    """"""
    __tablename__ = "expenses"
 
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(50))
    category = Column(String(50))
    description = Column(String(50))
    link = Column(String(50))
    estimated_costs = Column(Integer)
    submit_date = Column(String(50))
    status = Column(String(50))
    decision_date = Column(String(50))
 
    def __init__(self, name, email, category, description, link, estimated_costs, submit_date, status, decision_date):
        """"""
        self.name = name
        self.email = email
        self.category = category
        self. description = description
        self.link = link
        self.estimated_costs = estimated_costs
        self.submit_date = submit_date
        self.status = status
        self.decision_date = decision_date
 
if dbExists == false:
    # create tables
    Base.metadata.create_all(engine)
    # create a Session
    Session = sessionmaker(bind=engine)
    session = Session()
    # create data
    expense = Expense("Foo Bar","foo@bar.com", "office supplies|travel|training", "iPad for office use", "http://www.apple.com/shop/buy-ipad/ipad-pro", 700, "09-08-2016", "pending", "")
    session.add(expense)
    expense = Expense("Foo Bar","foo@bar.com", "office supplies|travel|training", "iPad for office use", "http://www.apple.com/shop/buy-ipad/ipad-pro", 700, "09-08-2016", "complete", "")
    session.add(expense)
    # commit the record the database
    session.commit()
    session.commit()