from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('portfolio/<int:id>', views.portfolio, name='portfolio'),
]