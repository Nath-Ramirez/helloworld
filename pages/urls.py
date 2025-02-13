from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView, ProductIndexView, ProductShowView, ProductCreateView, ProductSuccessView

urlpatterns=[
    path('',HomePageView.as_view(), name='home'),
    path('about/',AboutPageView.as_view(), name='about'),   #new
    path('contact/',ContactPageView.as_view(), name='contact'), #new
    path('products/', ProductIndexView.as_view(), name='index'),    #new
    path('products/create', ProductCreateView.as_view(), name='form'),  #new
    path('products/<str:id>', ProductShowView.as_view(), name='show'),  #new
    path('products/create/successful', ProductSuccessView.as_view(), name='successful'),  #new
]
