from django.urls import path
from Backend import views
urlpatterns=[
    path('intro/',views.intro,name="intro"),

    path('ad_category/', views.ad_category, name="ad_category"),
    path('save_category/', views.save_category, name="save_category"),
    path('cat_display/', views.cat_display, name="cat_display"),
    path('cat_edit/<catid>/',views.cat_edit,name="cat_edit"),
    path('cat_update/<catid>/',views.cat_update, name="cat_update"),
    path('cat_delete/<catid>/', views.cat_delete, name="cat_delete"),

    path('ad_product/', views.ad_product, name="ad_product"),
    path('save_product/', views.save_product, name="save_product"),
    path('pro_display/', views.pro_display, name="pro_display"),
    path('pro_edit/<proid>/', views.pro_edit, name="pro_edit"),
    path('pro_update/<proid>/', views.pro_update, name="pro_update"),
    path('pro_delete/<proid>/', views.pro_delete, name="pro_delete"),

    path('con_display/',views.con_display,name="con_display"),
    path('con_edit/', views.con_edit, name="con_edit"),

    path('login_page/',views.login_page,name="login_page"),
    path('admin_login/', views.admin_login, name="admin_login"),

]