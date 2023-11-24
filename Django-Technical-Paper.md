# Framework

- A framework is a pre-built, reusable set of libraries, tools, and conventions designed to help developers build s/w applications more efficienlty.
- A framework is a particular set of rules, ideas, or beliefs which you use in order to deal with problems or to decide what to do.

# Django

- Django is basically a high-level Python web application framework that enables the rapid development of web applications.
- Open-source Python framework.
- Follows the Model-View-Template (MVT) structural pattern.
- Most popular framework in Python

# Advantage of using django

- Fast and simple.
- It's secure.
- It suits any web application program.
- It's well established.
- MVT Support and Object-Oriented Approach.
- Built-in authentication and authorisation
- Packaging system.

# Pre-requisites

- Understanding the indentation and syntax of Python.
- HTML, CSS, and JavaScript.

# MVT

- Frameworks like LARAVEL, Spring, Ruby ... follows MVT(Model View Controller) pattern.
- Django follows MVT pattern.
- **MVT-**
- Model
  - A model is a Python class that defines the fields and behaviors of the data you're storing using **Django's ORM.**.
  - Each model(class) corresponds to a table in the database, and instances of the model(object) represent rows in the table.
  - Django models are used to interact with databases, and they provide an abstraction layer for database queries.
- Template
  - **Generates the HTML dynamically**, incorporating both static and dynamic content.
  - A template includes static parts, which are the fixed portions of the HTML output that do not change.
  - Templates **use special syntax** to describe how dynamic content from the views will be inserted.
- Views
  - Views are components that handle the **logic** of processing a user's request and returning an appropriate response.
  - A view receives data from the user, interacts with the necessary models to perform actions on the database if needed, and passes it to the templates, and then returns a response, often in the form of rendered HTML content.

Conclusion --

- User will send a request to django application server which will go to **URLs**
- And the URLs will check for views and inside the view we write the logic.
- The view will fetch or update data in the database(Models represent the data structure and handle database operations).
- And then after obtaining the necessary data from modets, the view passes this to a template(Models represent the data structure and handle database operations).
- The generated HTML, along with the processed data, is sent as a response to the user's initial request.
  ![MVT Flow chart](https://techvidvan.com/tutorials/wp-content/uploads/sites/2/2021/06/Control-Flow-Of-MVT.jpg)

# django-admin

- django-admin is a **command-line utility** that comes with **Django** and is used for various administrative tasks related to Django projects and applications.
- It provides a set of commands that allow you to manage database operations, create superusers, run development servers, and perform other administrative tasks.

- Creating a Django Project (run this cmd in the folder in which you have to make a new-project folder)

```
  django-admin startproject projectname
```

- Running Development Server: (to run this cmd you have to be in your root-folder where manage.py is present.)

```
  python3 manage.py runserver
```

- Command -- **pip freeze**

# Python Django Structure

- myProject
  - **media** --> Will contain dynamiic images and files
  - **static** --> Will contain static photos, CSS and JS files, font files
  - **template** --> Will contain the HTML files which will be used in our project
  - myproject --> App
    - **pycache**
    - **init**.py
    - asgi.py
    - **settings.py** --> Manages all the settings of our project
    - **urls.py** --> Manages all the URLs in our project which will be connected to our view functions later
    - **views.py** --> Contain different logics in separate functions/classes
  - wsgi.py
  - db.sqlite3 --> Default Database
  - **manage.py** --> **Main** file of our project

# Creating a Django app (Refer Geeky Shows -> Video-33)

- In here, creating an app means creating a separate module which will perform a specific functionality of our project.
- Steps

1. **Create a Django App:**

   - Django projects are made up of one or more apps. Each app is a self-contained module that can be reused in other projects.
   - (Run this command in the root folder of your project)

   ```bash
   python manage.py startapp yourappname
   ```

2. **Configure the App in the Project:**

   - Open the `settings.py` file in your project directory and add your app to the `INSTALLED_APPS` section:

   ```python
   INSTALLED_APPS = [
       # ...
       'yourappname',
   ]
   ```

3. **Define Models:**

   - In your app directory, open the `models.py` file and **define your data models using Django's ORM**. For example:
   - Here we imported **models module.** The main component within the "models" module is the **Model class** ( it provides built-in functionalities, fields ( eg..CharField, IntegerField, etc )), which is used to create classes representing database tables and their fields.
   - Each model which we create is a Python class that **subclasses django.db.models.Model.**
   - Each attribute of the model represents a database field.
   - Table name -- **ApplicationName_ClassName**

   ```python
   from django.db import models

   class YourModel(models.Model):
       field1 = models.CharField(max_length=100)
       field2 = models.IntegerField()
       # Add other fields as needed
   ```

4. **Run Migrations:**

   - Django uses migrations to manage changes to your database schema. Run the following commands in the root folder to apply the initial migrations:

   ```bash
   python manage.py makemigrations  # model classes -> sql queries/statements
   python manage.py migrate         # sql query/statement -> table in database
   ```

## Note ['Model' built-in class of 'models' module]

- Built-in field options -
  - null = True/False
  - default = 'default_value'
  - blank = True/False
  - verbose_name = 'Student Name'
  - primary_key = True/False
  - unique = True/False ....
- Built-in field Types
  - IntegerField
  - BigIntegerField
  - AutoField
  - FloatField
  - CharField
  - TextField
  - BooleanField
  - EmailField
  - URLField
  - BinaryField

# Migrations (Refer Geeky Shows -> Video-33)

- The initial migrations, often referred to as "default migrations," establish the initial state of your database based on your initial model definitions.
- In python we define data models in models.py file. Each model class represents structure of a table(rows, columns, datatypes) of the DB.

## Create Initial Migration:

```
python3 manage.py makemigrations
```

- Run this command to analyze our models and create a initial set of migrations files in the 'migrations' directory of our app.
- These migrations capture the changes to the database schema.

## Apply Migrations

```
python3 manage.py migrate
```

- After creating the initial migrations, you apply them to the database (db.sqlite file) using the **migrate** command.
- To create tables in database based on our models.
- To synchronise database with our models. (if we added now tables/ model classes in our models.py file)

# Object Relational Mapper [ORM] (Refer Geeky Shows -> Video-32)

- ORM enables applications(our apps) to interact with the databases such as SQLite, MySOL, PostgreSQL,Oracle.
- **Django works on ORM Pattern and ORM follows object-oriented approach.**
- ORMs automatically creates a database schema from defined classes/models (in models.py). So, for one who
  don't know SQL will find this very beneficial.
- **ORM generates/creates SQL query from python code** and manipulate your database and get results in **pythonic fashion**, which means developers do not need to write SQL code.
- ORM maps object attributes(columns) to respective table fields.
- We know that SQLite, MySOL, PostgreSQL, Oracle... these all database management systems have  
  dissimilarities in their SQL coding formats, but in ORM pattern we don't require SQL coding so it is
  easier to change database management system. Hence, ORM inhances portability.
- ORMs use **connectors** to connect databases with a web application.

# QuerySet (Refer Geeky Shows -> Video-86)

- A QuerySet can be defined as a list containing all those objects we have created using the Django model.
- QuerySet allow us to read the data from the database, filter it and order it.
- **Syntax-**

  - ModelClassName.objects.function()

  ```python
  from myapp.models import Person   # from models.py file in myapp folder import Person model/class.

  # Retrieve all Person class's objects from the database
  all_people = Person.objects.all()
  obj = Person.objects.get(it=0)
    ...
  # Filter the queryset to get people with age greater than 30
  older_people = Person.objects.filter(age__gt=30)
  ```

- QuerySets are generally associated with CRUD operations.
- **CRUD Http Operations:**

  1. C -> Create -> POST method
  2. R -> Read -> GET method
  3. U -> Update -> PUT method
  4. D -> Delete -> DELETE method

- To see the SQL query created by Django in the backend (to get a QuertSet object)
  - obj = Person.objects.get(it=0)
  - **We can use command ---> print('SQL QUERY:', obj.query)**

## QuerySet methods:

1. ModelClassName.objects.
2. .all(), .get(...), .filter(...), .exclude(...), .order_by(...), .reverse(), .distinct()
3. .values(), .values(..want specific columns..) -> converts our **QuerySet of objects into a QuerySet of
   dictionaries** containing the object.
4. .values_list(), .values(..want specific columns..) -> method is similar to .values(), but it returns a **QuerySet of tuples** instead of dictionaries.
5. QuerySet methods between two query sets:
   - q1.union(q2) --> full join (but returns distinct rows only)
   - q1.intersection(q2) --> innerjoin
   - q1.difference(q2) --> left join (swap q1 & q2 is want q2's left join)
   -

# Superuser

- In Django, a superuser is a user account with special privileges that allow them to access and manage the Django admin interface.
- **The Django admin is a powerful tool for managing the content of your site and performing administrative tasks.**

## Creating a Superuser:

```
python manage.py createsuperuser
```

## Enter Superuser Information:

```
Username: admin
Email address: admin@example.com
Password: **********
Password (again): **********
```

`Superuser created successfully.`

- Start the development server.
- Access the Django admin interface by navigating to http://localhost:{port_no}/admin/ in your web browser.
- Enter the superuser credentials (username, email, and password) you just created to log in to the Django admin interface.
- Once logged in, you'll have access to the admin interface where you can manage models, perform CRUD (Create, Read, Update, Delete) operations, and perform other administrative tasks for your Django project.

# Creating URLs[ROUTES] and Views

- A view receives a web request as input from the user and return a web response.

**1. Function-Based Views:**

```python
from django.http import HttpResponse

def my_view(request):
    return HttpResponse("Hello, this is my view!")          # View logic goes here
```

**2. Class-Based Views:**

- It is a more organized way to structure your code, especially for more complex views.
- Class-based views are often subclass from Django's built-in generic views.

```python
from django.views import View
from django.http import HttpResponse

class MyView(View):
    def get(self, request):
        return HttpResponse("Hello, this is my class-based view!")              # View logic goes here
```

**3. Request and Response Objects:**

- Views take a request object as a parameter, which contains information about the user's request (e.g., GET or POST parameters, headers).
- The view then returns a response object, indicating what should be sent back to the user.

**4. Rendered Templates: (Rendering HTML Template as Response)**

- Step1: Create a html-file in the template folder inside the main project-folder.
- Step2: Go to settings.py and add the template folder path to TEMPLATES array. **'DIRS': [BASE_DIR,'templates']**
- Step3: Go to views.py and add the logic to render HTML template. (import the **render** function from shortcuts.py file of django )

  ```python
    from django.shortcuts import render

    def homePage(request):
      return render(request,'index.html')    # render(request,html_file_name)
  ```

- Step4: Then add path to this view in urlpatterns array of urls.py file.

**5. Passing Data from Django View to a Template**

- For passing data from Django view to a Template first we have to make a dictionary(containing data) in the view function/class and pass that dictionary to the render function as a parameter.

  ```python
  from django.shortcuts import render
  def homePage(request):
      data = {
          'title' : 'Home Page',
          'heading': 'Welcome to my Webpage'
          'available_courses': ['JAVA','Python','C++']    # to use this list's data in the html template we have to use for loops in html template
          'student_detail': [
            {'name':'pradeep','phone':12345678},
            {'name':'sandeep','phone':87654321}
          ]
      }
      return render(request,'index.html',data)
  ```

- Dictionary format -
  ```python
  dict_name = {
    'key': 'value'
      ...
  }
  ```
- And in the **html template** whereever we need data we can fetch it using **{{ ... }}**

**6. URL Mapping:**

- Views are mapped to specific URLs in the urls.py file of your Django app.
- The **URL dispatcher** is responsible for matching the requested URL to the appropriate view.

```python
from django.urls import path
from .views import my_view

urlpatterns = [
    path('my-url/', my_view, name='my-url-name'),
]
```

**7. Create Dynamic URLs/Routes in Django**

```python
from django.urls import path
from . import views

urlpatterns = [
    path("articles/2003/", views.special_case_2003),
    path("articles/<int:year>/", views.year_archive),
    path("articles/<data>/", views.show_data),
    path("articles/<int:year>/<int:month>/", views.month_archive),
    path("articles/<int:year>/<int:month>/<slug:slug>/", views.article_detail),
]
```

# HTML templates

**NOTE- Referring the data sent from the view function to html template**

## for loops on a list

```django html
{% for course in available_courses %}
   <div>{{course}}</div>
{% endfor %}
```

## for loops on a dictionary

```django html
<table border="1" cellpadding="10" >
    <tr>
        <th>Name</th>
        <th>Phone number</th>
    </tr>

    {% for obj in student_details %}
    <tr>
        <td>{{obj.name}}</td>
        <td>{{obj.phone}}</td>
    </tr>
    {% endfor %}
</table>
```

## if..elif..else

```django html
{% if available_courses|length > 0 %}
    {% for course in available_courses%}
        <div>{{forloop.counter}} {{course}}</div>       <!-- forloop.counter, .counter0, .revcounter, .revcounter0, .first, .last -->
    {% endfor %}
{% else %}
    Empty list
{% endif %}
```

# Managing static files(e.g. images, JavaScript, CSS)

- Step1: Create a folder named 'static' inside our project-folder.
- Step2: Add all the static content to this folder
- Step3: Go to settings.py and add the 'static' folder's path to **'STATICFILES_DIRS'**:
  ```python
  STATICFILES_DIRS = [
    BASE_DIR,"static"
  ]
  ```
- Step4: Go to html-templates and change the href's and src's of html-tags(like links, images, etc) to refer to static files present in static-folder
  - Way-1: Simply do :-
    ```html
    example -
    <link rel="stylesheet" href="/static/home_page_style.css" />
    <img src="/static/Home_page_images/education-training.png" alt="" />
    ```
  - Way-2: **Use static-tag of django:-**

    - The {% static %} tag is used to generate the URL for a static file, such as a CSS file, JavaScript file, image, or any other static asset.
    - Use ---> **{% load static %}**

    ```django html
    {% load static %}    <!--Write this in the top to load static URLs-->

    <img src="{% static '/Home_page_images/tree-planting.png' %}" alt="" />
    ```

# Header and Footer in Django HTML Template [{% include %} tag]

- In general top and bottom part of all the pages of a website are same, so instead of writing it's code multiple times in each page's html code, simply write this code in header.html and footer.html template and **include** it in the website page's html files.
- The **{% include %} tag** is used to include the content of another template within the current template.

  ```django html
  <!-- main_template.html -->
  {% include 'header.html' %}

  <main>
      <h2>Main Content Goes Here</h2>
      <!-- Your main content goes here -->
  </main>

  {% include 'footer.html' %}
  ```

# How to use Extends and Include Django Template Tags

1. Create a base.html file in template folder.
2. **include** header and footer in this.
3. Inbetween header and footer add **block tag**.
4. Go to our webpage's html template.
5. Remove include tags (if any).
6. Then extend the base.html template using **extends tag**.
7. Then enclose the remaining content in the **block tag**.

- base.html file:

  ```django html
  {% include "header.html" %}
  {% block content %}
  <!-- Content of our webpage will be fetched here -->
  {% endblock %}
  {% include "footer.html" %}
  ```

- Our index.html file:
  ```django html
  {% extends "base.html" %}
  {% block content %}
      <div class="intro">
        <p>#STOP CLIMATE CHANGE</p>
        ....content...
  {% endblock %}
  ```
