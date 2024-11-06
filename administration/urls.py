from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('panel/', views.panel, name='panel'),
    path('search/', views.search, name='search'),
    path('administration/', views.administration, name='administration'),
    path('erase/', views.erase, name='erase'),
]
