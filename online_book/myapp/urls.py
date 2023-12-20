from django.urls import path
from myapp import views

urlpatterns = [
    path('home/', views.find, name='search'),
    path("data_entry/", views.data, name='data'),
    path('update/<int:id>', views.update, name='update'),
    path("<int:id>", views.delete, name='delete'),
    path('cart/', views.Cart_search, name='cart'),
    path('addtocart/', views.add_to_cart, name='addtocart'),
    path('viewcart/', views.view_cart, name='viewcart'),
    path('remove/<int:id>', views.Remove_cart, name='remove_cart'),
    path('cart_inc/', views.cart_increase, name='cart_inc'),
    path('cart_dec/', views.cart_decrease, name='cart_dec'),
    path('login/', views.Login, name='login'),
    path('logout/', views.LogOut, name='logout'),
    path('signup/', views.Signup, name="signup"),
    path('orderplace/', views.Order_place, name='orderplace'),
    path('address/', views.address_user, name='address'),
    path('cart_order/',views.Order_place1,name='cart_order')
]