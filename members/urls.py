from django.urls import path

from members.views import register, main_page, signup


urlpatterns = [
    path('register/', register, name ='register'),
    path('', main_page, name='main'),
    path('signup/', signup, name='signup'),

]