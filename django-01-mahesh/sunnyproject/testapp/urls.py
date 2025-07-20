from django.urls import path
from . import views

urlpatterns = [
    path('exam/',views.exam_view),
    path('attendance/',views.attendance_view),
    path('fee/',views.fee_view),
]