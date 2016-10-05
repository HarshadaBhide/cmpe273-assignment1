from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
 
# Database Configurations
app = Flask(__name__)
DATABASE = 'assign1'
PASSWORD = 'root'
USER = 'root'
HOSTNAME = 'cmpe273assignment1_db_1'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://%s:%s@%s/%s'%(USER, PASSWORD, HOSTNAME, DATABASE)
db = SQLAlchemy(app)

class Expense(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(50))
    category = Column(String(50))
    description = Column(String(50))
    link = Column(String(50))
    estimated_costs = Column(String(50))
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