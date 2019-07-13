from herokuapp import views
from django.urls import path




urlpatterns = [
    path('', views.index, name='index'),
    path('category/<slug:category_name_url>/', views.category, name='category'),
    path('add_category/', views.add_category, name='add_category'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('restricted/', views.restricted, name='restricted'),
    path('logout/', views.user_logout, name='logout'),
    path('category/<slug:category_name_url>/add_page/', views.add_page, name='add_page'),
    path('about/', views.about, name='about'),
    path('about_fbsg/', views.about_fbsg, name='about_fbsg'),
    path('Shop/', views.Shop, name="Shop"),

]
