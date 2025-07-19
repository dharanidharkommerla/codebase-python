from django.urls import path
# import views
# from testapp import views
from . import views
# "." represent same directory

urlpatterns = [
    path('first/', views.first_view),
    path('second/', views.second_view),
    path('third/', views.third_view)
]