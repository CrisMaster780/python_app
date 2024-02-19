from django.urls import path
from .views import index_presupuesto

urlpatterns = [
    path('', index_presupuesto, name='presupuesto'),
   
]