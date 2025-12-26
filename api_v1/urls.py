from django.urls import path
from api_v1 import views

urlpatterns = [
    path('get_token/', views.get_token_view, name='get_token'),
    path('add/', views.add, name='add'),
    path('subtract/', views.subtract, name='subtract'),
    path('multiply/', views.multiply, name='multiply'),
    path('divide/', views.divide, name='divide'),
]