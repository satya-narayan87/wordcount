from django.urls import path
from . import views

urlpatterns = [
    path("",views.home_page),
    path("contact",views.contact_us)
]
