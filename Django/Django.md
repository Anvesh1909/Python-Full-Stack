# Django
## Prerequest to learn Django
- FrontEnd Technologies
    - HTML and HTML5
    - CSS and CSS3
    - JavaScript
    - Bootstrap
    - Angular
    - ReactJS
- Programming Language  
    - core python 
    - advance python 
    
---
## what is django
- django is a backend webframework
- the main objective of django framework is to develop complete end to end web application
- A django developer is responsible for presentation logic, business logic and presistance logic. 
- data base logic.
- django uses its own wen server named as wsgi/awsgi
    - web server gateway interface
    - which runs on port number 8000

### MVT architecture
- Django uses design pattern named as MVT
- MVT stands for Model View Template
    - M -> it is a class in django used for database operations
    - V -> meant for to write the business logic for request and responce operation using following components
        - Using functional component
        - using class component
    - T -> meant for fontend development using templates we can use html and html5 to represent content on the web page
        - static stores images,js and css files
- django uses its own database named as SQLITE3
- we can configure other databases as well as per the application requirement

---
## commands to start a django project
- django uses CLI ( command line interface (cmd)) approach
- to uninstall `pip uninstall django`
- to install `pip install django`
- to check version `django-admin --version`
- to check all commands `django-admin`
    ```
    django-admin

    Type 'django-admin help <subcommand>' for help on a specific subcommand.

    Available subcommands:

        [django]
        check
        compilemessages
        createcachetable
        dbshell
        diffsettings
        dumpdata
        flush
        inspectdb
        loaddata
        makemessages
        makemigrations
        migrate
        optimizemigration
        runserver
        sendtestemail
        shell
        showmigrations
        sqlflush
        sqlmigrate
        sqlsequencereset
        squashmigrations
        startapp
        startproject
        test
        testserver
    ```
- to create a project `django-admin startproject appname`
    - ex `django-admin startproject baseproject`
```

baseproject
├───baseproject
│   ├───__init__.py
│   ├───asgi.py
│   ├───settings.py
│   ├───urls.py
│   └───wsgi.py
├───manage.py

```
- `__init__`.py -> this is empty file which indicates it is package in django
- settings.py -> this file contains django project settings
- urls.py -> this file contains the urls which is used for routing to views. it is meant for the end user to access our application services
- wsgi.py -> this file is meant for deployment purpose or protection purpose
- manage.py -> 
    - it is used to create the applications inside the project 
    - to run the webserver
    - to update database
---
- `cd project projectname`
- to run a web server `python manage.py runserver`
- to change the port number `python manage.py runserver 8888`
- create an application in python `python manage.py startapp appname`
    - ex: `python manage.py startapp app1`
    - migrations folder -> is used for database operations
    - `__init__`.py -> is used for to indicate it is a application package
    - admin.py -> this file is used to add the database instances inside the admin app
    - apps.py -> this file is used to perform end to end testing operations as per the application requirment
    - models.py -> this file is used to create one or more than one database table(models) for django web application.
    - tests.py -> this file is used to perform unit testing operations   
    - views.py -> this file is used for to write the business logic for request and responce operations using following components
        - using functional component
        - using class component
```
baseproject
├───baseproject
│   ├───__init__.py
│   ├───asgi.py
│   ├───settings.py
│   ├───urls.py
│   └───wsgi.py
├───app1
│   ├───__init__.py
│   ├───admin.py
│   ├───app.py
│   ├───models.py
│   ├───tests.py
│   └───views.py
├───manage.py

```

--- 

- go to setting.py
    - inside the installed_apps add appname
    - ex: 
    ```python
    INSTALLED_APPS = [
            "django.contrib.admin",
            "django.contrib.auth",
            "django.contrib.contenttypes",
            "django.contrib.sessions",
            "django.contrib.messages",
            "django.contrib.staticfiles",
            "app1"
        ]
    ```
- go to views.py
    - import `from django.http import HttpResponse`
    - create a function with a parameter `request` request contains front user data
    - and `return HttpResponse('Any text')`
    - ex:
    ```python
    from django.http import HttpResponse

    def index(request):
        return HttpResponse("This is the First Responce")
    ```
    - inside url import views
        - and give `path("",views.index)`
    - ex:
    ```python
    from django.contrib import admin
    from django.urls import path
    from app1 import views

    urlpatterns = [
        path("admin/", admin.site.urls),
        path("",views.index),
    ]

    ```
    - we can also use html tags inside the httpresponce 
    - but we do have a template folders to to write frontend files 
    - 
- Class Component
- 
```python
# views.py
from django.views import View
from django.http import HttpResponse

class IndexClass(View):
    '''
        "get","post","put","patch","delete","head","options","trace",
    '''
    def get(self,request):
        return HttpResponse("<h1>Class Component Get</h1>")


# urls.py
from django.contrib import admin
from django.urls import path
from app1.views import index
from app2.views import IndexClass

urlpatterns = [
    path("admin/", admin.site.urls),
    path("FunctionalComponent",index),
    path("ClassComponent",IndexClass.as_view()),
]
   
        
```

---
- develop a django project which contains one application use views.py using functional component and class component


---
# Working on Templates 
in django template is meant for front end development
- inside the templates we can put html and html5 files to represent content on the web page
- inside the application no need to change the setting if the templates not in application
- inside templates dir `os.path.join('BASE_DIR','templates')`

---
# working on static folder 
- static folder contains the following folders 
    - images
    - css
    - js
- inside the application no need to change the setting if the static not in application
- inside templates dir `staticDIR = os.path.join('BASE_DIR','static')`
- 
```python
STATICFILES_DIRS = [
    BASE_DIR / "static",
    os.join.path(BASE_DIR,"static")
]
```

---


# how to create loginForm in django with client side validation

---
# model
- model is a class in django
- the main objective of model is to create one or more than one database tables 
```python
from django.db import models

# Create your models here.
class Students(models.Model):
    rollNo = models.IntegerField(null=False,unique=True)
    name = models.CharField(max_length=200)
    standard = models.IntegerField()
    presentage = models.FloatField()


    def __str__(self):
        return self.name
```
---
develop a django application create the model for student which consist of 10 records store the 10 records manually in the data base extract the complete data into the django web page using class component

---
how to connect django with mysql database 
- need to install pymysql 
```python
DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'DjangoCon',
        'USER': 'root',
        'PASSWORD': 'Anv@14078',
        'HOST' : '127.0.0.1',
        'PORT' : '3306'
    }
}
```

## Assignment
- develop one django application using complete frontend and backend including template and static folder and creat models and extract data from mysql to our django web page

---
## working on forms module in django 
```python
from django import forms

class StudentsForm(forms.Form):
    rollNo = forms.IntegerField()
    name = forms.CharField(max_length=200)
    standard = forms.IntegerField()
    presentage = forms.FloatField()
```

- develop a django application to create the complete employee registration form using django forms 

---
## Exception handling in django
- predefiend Exception
- Custom or user defined exception
- the main objective of user defiend exception is to display the meaningfull output a end user can easily understand 
- develop a django application develop a logic in such a way that for custom or userdefined exception by writing try except and finally block
---
## cookies in django 
- cookies are small piece of information created by django webserver 
- resides in client machine(our own operating system)
- in django once the cookies are ready client autometically write the cookies
- in django all cookies are represent in dictionary format 
### how to set the cookies
- we can set the cookies using following methods 
- `set_cookie("cookie_name","cookie_value")`
### how to get the cookies
- we can get the cookies using following methods 
- `request.COOKIES.get("name","Else_default message")`
### delete cookies
- `delete_cookies("name")`

---
- develop a django application for cookies management system
  - using functional component
  - using class component
---
## one to many or many to one relation 
- develop a django application for one to many or many to one relationships
- artical - reporter
---
# many to many relationship 
- customer - product
- develop a django application which satisfies the following relationships
