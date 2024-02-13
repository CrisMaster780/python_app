from django.urls import path
from .views import home_index

urlpatterns = [
    path('', home_index, name='home'),
]
