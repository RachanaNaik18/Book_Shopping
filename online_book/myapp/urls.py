from django.urls import path
from myapp import views

urlpatterns = [
    path('home/', views.find, name='search'),
    # path("home/", views.Home, name='home'),
    path("data_entry/", views.data, name='data'),
    path('update/<int:id>', views.update, name='update'),
    path("<int:id>", views.delete, name='delete'),
    path('cart/', views.Cart_search, name='cart'),
    path('addtocart/', views.add_to_cart, name='addtocart'),
    path('viewcart/', views.view_cart, name='viewcart')
]