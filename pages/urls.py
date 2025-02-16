from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView, ProductIndexView, ProductShowView, ProductCreateView, ProductSuccessView, CartView, CartRemoveAllView

urlpatterns=[
    path('',HomePageView.as_view(), name='home'),
    path('about/',AboutPageView.as_view(), name='about'),   
    path('contact/',ContactPageView.as_view(), name='contact'), 
    path('products/', ProductIndexView.as_view(), name='index'),    
    path('products/create', ProductCreateView.as_view(), name='form'),  
    path('products/<str:id>', ProductShowView.as_view(), name='show'),  
    path('products/create/successful', ProductSuccessView.as_view(), name='successful'),  
    path('cart/', CartView.as_view(), name='cart_index'),   #new
    path('cart/add/<str:product_id>', CartView.as_view(), name='cart_add'), #new
    path('cart/removeAll', CartRemoveAllView.as_view(), name='cart_removeAll'), #new
]
