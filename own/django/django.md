django framework
full stark application 
frontend backend

django built upon python

django follows MVT architecture 
M - Model : database schema (tables)
V - Views : backend logic (what should be rendered and input and output to the frontend)
T - Templates : stores frontend ( Html,css,js,media )

---
Virtual environment
isolates the dependencies(libraries) required for a projects

install venv
pip install virtualenv

to create venv
python -m venv practice

to activate venv
practice\Scripts\activate


--- 
install django
pip install django


start project
django-admin startproject projectname


inside the project a folder name same with the project name
- that is main project
- setting.py -> all configarations are witten
- urls.py -> to write routes


inside a project we can create multiple smaller apps
to create apps inside the project
- python manage.py startapp appname

to check installation successfully
python manage.py runserver

inside app create a folder templates
inside the template a basic templates hello world

to insert that app into project 
go to setting.py
write appname inside the 

INSTALLED_APPS


to render 
we should write logic inside the views.py

any application will work on request , responce cycle

add students route to urls.py
and written login in views.py




database connection ( Models )
students 
id name batch course
id primary key() -> automaticly given by django



create table 
python manage.py makemigrations
- convert python language to sql quaries 
python manage.py migrate
- execute sql quaries




to tansfer data from backend to frontend
we use context dict and send it from render
and use in html page


to insert data in the table 
create an admin user
python manage.py createsuperuser


we need to register student table in admin page(admin.py)

from students.models import Students

admin.site.register(Students)