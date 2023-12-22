from django.urls import path
from . import views


urlpatterns = [
    path('', views.my_first_view, name='my_first_view')
]
