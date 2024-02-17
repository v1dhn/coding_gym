from django.contrib import admin
from django.urls import path, include
from coding_problems.views import home





urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('', include('coding_problems.urls')),
]
