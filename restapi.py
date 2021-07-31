from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
# from json import dumps
from flask_jsonpify import jsonify
from person import Person

db_connect = create_engine('sqlite:///D:\\Software\\sqlite\\db\\chinook.db')
app = Flask(__name__)
api = Api(app)

class Employees(Resource):
    def get(self):
        conn = db_connect.connect() # connect to database
        query = conn.execute("select * from employees") # This line performs query and returns json result
        result = {'employees': [i[1] for i in query.cursor.fetchall()]} # Fetches first column that is Employee ID
        return result

    def post(self):
        conn = db_connect.connect()
        print(request.json)
        LastName = request.json['LastName']
        FirstName = request.json['FirstName']
        Title = request.json['Title']
        ReportsTo = request.json['ReportsTo']
        BirthDate = request.json['BirthDate']
        HireDate = request.json['HireDate']
        Address = request.json['Address']
        City = request.json['City']
        State = request.json['State']
        Country = request.json['Country']
        PostalCode = request.json['PostalCode']
        Phone = request.json['Phone']
        Fax = request.json['Fax']
        Email = request.json['Email']
        query = conn.execute("insert into employees values(null,'{0}','{1}','{2}','{3}', \
                            '{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}', \
                            '{13}')".format(LastName,FirstName,Title,
                            ReportsTo, BirthDate, HireDate, Address,
                            City, State, Country, PostalCode, Phone, Fax,
                            Email))
        return {'status':'success'}

class Employees_Name(Resource):
    def get(self, employee_id):
        conn = db_connect.connect()
        query = conn.execute("select * from employees where EmployeeId =%d "  %int(employee_id))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class Tracks(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select trackid, name, composer, unitprice from tracks;")
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class Importtest(Resource):
    def get(self):
        p1 = Person('Umesh Patra')        
        return 'test from importtest :' + p1.myfunc()

api.add_resource(Tracks, '/tracks')
api.add_resource(Employees, '/employees')
api.add_resource(Employees_Name, '/employees/<employee_id>') # Route_3
api.add_resource(Importtest, '/importtest')

if __name__ == '__main__':
    app.run(port='5002')