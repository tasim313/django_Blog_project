from django.urls import path
from .import views

app_name = 'App_Login'

urlpatterns = [
    path('sign_up/', views.sign_up, name='sign_up'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('change_profile/', views.profile_change, name='change_profile'),
    path('password/', views.user_password_change, name='password_change'),
    path('add_profile_pic/', views.add_profile_pic, name='add_profile_pic'),
    path('change_profile_pic/',views.change_profile_pic, name='change_profile_pic'),

]
