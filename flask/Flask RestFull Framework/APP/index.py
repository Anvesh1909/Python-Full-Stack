from shutil import register_unpack_format
from flask import Flask
from flask_restful import Api,Resource

app = Flask(__name__)

api = Api(app)

class Home(Resource):
    def get(self):
        return {
            'data' : 'welcome to flask restful for api development' ,
            'hello' : True,
            'date' : None
        }
    
api.add_resource(Home,'/home')



class GetName(Resource):
    def get(self,name):
        return {
            'name' : f'myname is {name}'   
        }
    
api.add_resource(GetName,'/getname/<string:name>')



class StudentDetails(Resource):
    students = {
        1 : "Anvesh",
        2 : 'Surya',
        3 : 'Nikhil',
        4 : 'Prerana',
        5 : 'Ajay'
    }

    def get(self):
        return StudentDetails.students
    
api.add_resource(StudentDetails,'/students')



if __name__=="__main__":
    app.run(debug=True)
