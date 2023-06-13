from . import views
from django.urls import path

urlpatterns = [
    path("january", views.monthly_calander)
]