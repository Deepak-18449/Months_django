from django.urls import path
from . import views


urlpatterns = [
    # path('jan',views.jan),
    # path('feb',views.feb),
    path('', views.index),
    path('<int:month>', views.Month_by_number),
    path('<str:month>', views.Month_by_name ,name="month-challenge"),
]