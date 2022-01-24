# Simple_REST_API_using_Django

## Table of Contents:
1. [Install Django and DRF](#install-django-and-drf)
2. [Create Django Project and App](#create-django-project-and-app)
3. [Create Django Model](#create-django-model)
4. [Create DRF Serializer](#create-drf-serializer)
5. [Setup View and URL](#setup-view-and-url)

## Install Django and DRF

Let's start by creating virtual environment and activating it.

In MacOS:
```
$ python3 -m venv drf
$ source drf/bin/activate
```
In Windows:
```
C:\> python venv drf
C:\> drf\Scripts\activate.bat
```

Now install django and djangorestframework.

```
$ pip install Django==3.2.8
$ pip install djangorestframework==3.12.4
```

## Create Django Project and App

Create django project using the below command.

```
(drf) $ django-admin startproject restapi
```

Project will be created with the below folder structure.

```
restapi
|-- restapi
|  |-- __init__.py
|  |-- asgi.py
|  |-- settings.py
|  |-- urls.py
|  |-- wsgi.py
|-- manage.py
```
Now, move into restapi folder and create 'tutorials' app using the below mentioned commands.

```
(drf) $ cd restapi
(drf) $ python manage.py startapp tutorials
```

Folder structure looks like below.

```
restapi
|-- restapi
|  |-- __init__.py
|  |-- asgi.py
|  |-- settings.py
|  |-- urls.py
|  |-- wsgi.py
|-- tutorials
|  |-- migrations
|  |-- __init__.py
|  |-- admin.py
|  |-- apps.py
|  |-- models.py
|  |-- tests.py
|  |-- views.py
|-- manage.py
```
After the app is created, let’s register the app by adding the path to the app config in the restapi/settings.py. Also add 'rest_framework' to this list.

```
INSTALLED_APPS = [
...
    ‘rest_framework’,
    'tutorials'
]
```

Now, to make the app up, run the below command.

```
(drf) $ python manage.py runserver
Django version 3.2.8, using settings 'restapi.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

If everything goes as mentioned, you will see a message as show above.
Now, if you go to http://127.0.0.1:8000/ in the browser, you should see the success message.

## Create Django Model

Class in django Model is similar to a table in database. Let’s create 'Tutorial' class into tutorials/models.py.

```
from django.db import models


class Tutorial(models.Model):
   name = models.CharField(max_length=100)
   author = models.CharField(max_length=100)
   price = models.CharField(max_length=100)
```


Next, run the migrations to let Django know that we are going to add a new table to the database.

```
(drf) $ python manage.py makemigrations
(drf) $ python manage.py migrate
```

## Create DRF Serializer

Serialization is the process of converting database table into JSON format. Now we have to tell django rest framework how to serialize our model(Tutorial).

Now, create a new file with name 'serializers.py' under tutorials folder and the below code to tutorials/serializers.py.

```
from rest_framework import serializers
from .models import Tutorial


class TutorialSerializer(serializers.ModelSerializer):
   class Meta:
       model = Tutorial
       fields = ('name', 'author', 'price')
```


## Setup View and URL

Now let's create a view that provides data to the API endpoint (URL).

Add the below code to tutorials/views.py file.

```
from rest_framework import viewsets
from .serializers import TutorialSerializer
from .models import Tutorial


class TutorialViewSet(viewsets.ModelViewSet):
   queryset = Tutorial.objects.all()
   serializer_class = TutorialSerializer
```

Now ViewSet is ready to provide data and what we need is a URL as API endpoint.

To do that, create a new file 'tutorials/urls.py' and add the below code.

```
from django.urls import include, path
from rest_framework import routers
from .views import TutorialViewSet

router = routers.DefaultRouter()
router.register(r'tutorial', TutorialViewSet)

urlpatterns = [
   path('', include(router.urls)),
]
```

Finally let's link 'tutorials/urls.py' to 'restapi/urls.py' file.
Add the below code to 'restapi/urls.py' file.

from django.urls import path, include

```
urlpatterns = [
   path('admin/', admin.site.urls),
   path('', include('tutorials.urls')),
]
```


## Using the API

Run `python manage.py runserver` in your terminal and go to http://127.0.0.1:8000/tutorial/ in your browser.

Now you can use this page to make GET or POST requests. You can also use other apps like `postman` to test your api.
