from django.urls import path

from .views import agency, banana, fast, funflat, stand

urlpatterns = [
    path('agency', agency , name='agency'),
    path('banana', banana , name='banana'),
    path('fast', fast , name='fast'),
    path('funflat', funflat , name='funflat'),
    path('stand', stand , name='stand'),
]
