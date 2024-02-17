from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path('login/', LoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('register/', views.register_view, name='register'),
    path('problems/', views.list_problems, name='list_problems'),
    path('problems/<int:problem_id>/', views.show_problem, name='show_problem'),
    path('problems/<int:problem_id>/submit/', views.submit_solution, name='submit_solution'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
]
