from flask import Flask
from flask import request
from flask import session
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model import *
import simplejson as json
from sqlalchemy.exc import IntegrityError
import os

app = Flask(__name__)
app.debug = True

DATABASE = 'assign1'
PASSWORD = 'root'
USER = 'root'
HOSTNAME = 'cmpe273assignment1_db_1'
import sqlalchemy
engine = sqlalchemy.create_engine('mysql+pymysql://%s:%s@%s'%(USER, PASSWORD, HOSTNAME))
#engine.execute("DROP DATABASE %s "%(DATABASE))
engine.execute("CREATE DATABASE IF NOT EXISTS %s "%(DATABASE))
db.create_all()
# create data
expense1 = Expense("Foo Bar","foo@bar.com", "office supplies|travel|training", "iPad for office use", "http://www.apple.com/shop/buy-ipad/ipad-pro", 700, "09-08-2016", "pending", "")
db.session.add(expense1)
expense2 = Expense("Laptop","sales@dell.com", "Office Work", "Laptop for office use", "http://www.dell.com", 400, "09-18-2016", "complete", "")
db.session.add(expense2)
db.session.commit()

@app.route("/")
def hello():
    return "Hello from Bhide Flask App!!"

@app.route('/v1/expenses', methods=['POST'])
def addExpense():
    try:
        object = json.loads(request.data)
        expense = Expense(object['name'], object['email'],object['category'], object['description'], object['link'], object['estimated_costs'], object['submit_date'], "pending", "")
        db.session.add(expense)
        db.session.commit()
        record = db.session.query(Expense).filter_by(id=expense.id)
        data = {
            'id' : record[0].id,
            'name' :  record[0].name,
            'email' : record[0].email,
            'category' : record[0].category,
            'description' : record[0].description,
            'link' : record[0].link,
            'estimated_costs' : record[0].estimated_costs,
            'submit_date' : record[0].submit_date,
            'status' : record[0].status,
            'decision_date' : record[0].decision_date
        }
        resp = jsonify(data)
        resp.status_code = 201
        resp.headers.set('status', '201 Created')
        return resp
    except IntegrityError:
        return json.dumps({'status':'Error inserting record'})

@app.route("/v2/expenses/<expense_id>", methods=['GET', 'PUT', 'DELETE'])
def test(expense_id):
    if request.method == 'GET':
	    return 'GET ' + expense_id
    if request.method == 'PUT':
	    return 'PUT ' + expense_id
    if request.method == 'DELETE':
	    return 'DELETE ' + expense_id

@app.route("/v1/expenses/<expense_id>", methods=['GET', 'PUT', 'DELETE'])
def viewExpense(expense_id):
    if request.method == 'GET':
        try:
            record = Expense.query.filter_by(id=expense_id).first_or_404()
            data = {
                'id' : record.id,
                'name' :  record.name,
                'email' : record.email,
                'category' : record.category,
                'description' : record.description,
                'link' : record.link,
                'estimated_costs' : record.estimated_costs,
                'submit_date' : record.submit_date,
                'status' : record.status,
                'decision_date' : record.decision_date
            }
            resp = jsonify(data)
            resp.status_code = 200
            resp.headers.set('status', '200 OK')
            return resp
        except IntegrityError:
            return json.dumps({{'status':'Error fetching record'}})
    if request.method == 'PUT':
        try:
            record = Expense.query.filter_by(id=expense_id).first_or_404()
            object = json.loads(request.data)
            if 'name' in object:
                record.name = object['name']
            if 'estimated_costs' in object:
                record.estimated_costs = object['estimated_costs']
            if 'email' in object:
                record.email = object['email']
            if 'category' in object:
                record.email = object['category']
            if 'description' in object:
                record.email = object['description']
            if 'link' in object:
                record.email = object['link']
            if 'submit_date' in object:
                record.email = object['submit_date']
            if 'status' in object:
                record.email = object['status']
            if 'decision_date' in object:
                record.email = object['decision_date']
            
            db.session.commit()
            data = '202 Accepted'
            resp = jsonify(data)
            resp.status_code = 202
            resp.headers.set('status', '202 Accepted')
            return resp
        except IntegrityError:
            return json.dumps({{'status':'Error updating record'}})

    if request.method == 'DELETE':
        try:
            record = Expense.query.filter_by(id=expense_id).first_or_404()
            db.session.delete(record)
            db.session.commit()
            data = '204 No Content'
            resp = jsonify(data)
            resp.status_code = 204
            resp.headers.set('status', '204 No Content')
            return resp
        except IntegrityError:
            return json.dumps({{'status':'Error deleting record'}})

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')