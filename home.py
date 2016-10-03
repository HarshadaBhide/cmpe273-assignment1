from flask import Flask
from flask import request
from flask import session
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from createTable import *

app = Flask(__name__)
app.debug = True
app.secret_key = 's3cr3t'

db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/assign1'
db.init_app(app)
engine = create_engine('mysql://root:root@localhost:3306/assign1', echo=False)
Session = sessionmaker(bind=engine)
session = Session()

@app.route("/")
def hello():
    return "Hello from New5 Flask App!!"
	
@app.route('/v1/expenses', methods=['POST'])
def addExpense():
    POST_NAME = str(request.form['name'])
    POST_EMAIL = str(request.form['email'])
    POST_CAT = str(request.form['category'])
    POST_DES = str(request.form['description'])
    POST_LINK = str(request.form['link'])
    POST_ECOST = str(request.form['estimated_costs'])
    POST_SDATE = str(request.form['submit_date'])
    expense = Expense(POST_NAME, POST_EMAIL, POST_CAT, POST_DES, POST_LINK, POST_ECOST, POST_SDATE, "pending", "")
    session.add(expense)
    session.commit()
    #latestId = connection.insert_id()
    record = session.query(Expense).filter_by(id=expense.id)
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

@app.route("/v1/expenses>?expense_id=<expense_id>/", methods=['GET', 'PUT', 'DELETE'])
@app.route("/v1/expenses/expense_id=<expense_id>/", methods=['GET', 'PUT', 'DELETE'])		
@app.route("/v1/expenses/<expense_id>/", methods=['GET', 'PUT', 'DELETE'])
@app.route("/v1/expenses/<string:expense_id>/", methods=['GET', 'PUT', 'DELETE'])
@app.route("/v1/expenses/{expense_id}", methods=['GET', 'PUT', 'DELETE'])
def viewExpense(expense_id):
    if request.method == 'GET':
        record = session.query(Expense).filter_by(id=expense_id)
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
        resp.status_code = 200
        resp.headers.set('status', '200 OK')
        return resp

    if request.method == 'PUT':
        #ecost = request.args.get('estimated_costs', '')
        #ecost = request.args['estimated_costs']
        record = session.query(Expense).filter_by(id=expense_id)
        if 'name' in request.args:
            record[0].name = request.args['name']
        if 'estimated_costs' in request.args:
            record[0].estimated_costs = request.args['estimated_costs']
        if 'email' in request.args:
            record[0].email = request.args['email']
        session.commit()
        data = '202 Accepted'
        resp = jsonify(data)
        resp.status_code = 202
        resp.headers.set('status', '202 Accepted')
        return resp

    if request.method == 'DELETE':	
        record = session.query(Expense).filter_by(id=expense_id)
        session.delete(record[0])
        session.commit()
        data = '204 No Content'
        resp = jsonify(data)
        resp.status_code = 204
        resp.headers.set('status', '204 No Content')
        return resp
	
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')