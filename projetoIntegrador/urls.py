from django.conf.urls import url
from .views import *

urlpatterns = [
    url('', technology_week, name='technology_week'),
]