from django.urls import path

from blog import views

urlpatterns = [
    path('post/',views.Posts_list, name = 'posts_list'),
    # path('post/single',)
]