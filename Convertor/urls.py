from django.urls import path
from .views import getInput
urlpatterns = [
    path("", getInput, name="get_input")
]