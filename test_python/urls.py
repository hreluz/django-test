from django.conf.urls import url
from django.contrib import admin

#Importing the folder hours/views files and the function hours_index
from hours.views import hours_index


#When the user goes to the root path, it will go to the function hours_index
urlpatterns = [
    url(r'^', hours_index ,name='hours' ),
]
