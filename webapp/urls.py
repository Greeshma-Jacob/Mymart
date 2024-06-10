from django.urls import path
from webapp import views
urlpatterns=[
    path('home/',views.homepage,name="home"),
    path('about/', views.aboutpage, name="about"),
    path('our_products/', views.our_products, name="our_products"),
    path('products_filtered/<cat_name>/',views.products_filtered,name="products_filtered"),
    path('single/<int:pro_id>/', views.single, name="single"),

    path('contactpage/', views.contactpage, name="contactpage"),
    path('save_contact/',views.save_contact,name="save_contact"),


    path('add_cart/', views.add_cart, name="add_cart"),
    path('cart_page/', views.cart_page, name="cart_page"),
    path('delete_item/<int:p_id>/', views.delete_item, name="delete_item"),

    path('register/', views.register, name="register"),
    path('save_register/', views.save_register, name="save_register"),
    path('user_login/', views.user_login, name="user_login"),
    path('user_logout/', views.user_logout, name="user_logout"),
    path('member_login/', views.member_login, name="member_login"),
    path('checkout/', views.checkout, name="checkout"),
    path('payment/', views.payment, name="payment"),

]