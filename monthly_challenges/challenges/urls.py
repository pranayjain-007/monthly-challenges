from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index-page"),
    path("<int:month>", views.challenges_by_number),
    path("<str:month>", views.challenges_by_name, name="month-challenge")
]
