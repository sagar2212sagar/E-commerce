from django.urls import path
from .views import checkout,HomeView,ItemDetailView
app_name='core'
urlpatterns=[
    path('product/<slug>',ItemDetailView.as_view(),name='product'),
    path('',HomeView.as_view(),name='home'),
    path('checkout/',checkout,name='checkout'),
  
    
    ]