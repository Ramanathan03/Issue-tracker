from django.conf.urls import url, include
from accounts.views import user_login, user_register,logout, profile, edit_user_profile,changePassword



urlpatterns = [
    url(r'^login/$',user_login,name='login'),
    url(r'^register/$', user_register, name='register'),
    url(r'^logout/$',logout,name='logout'),
    url(r'^profile/$',profile, name='profile'),
    url(r'^profile/edit/$', edit_user_profile, name='editProfile'),
    url(r'^profile/password/$',changePassword, name='changePassword')
    ]