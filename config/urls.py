
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('members.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('post/', include('blog.urls')),

]
