from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home),
    path('Signup',views.Signup),
    path('Logout',views.logout),
]