from django.urls import path
from . import views

urlpatterns = [
    path('problems/', views.list_problems, name='list_problems'),
    path('problems/<int:problem_id>/', views.show_problem, name='show_problem'),
    path('problems/<int:problem_id>/submit/', views.submit_solution, name='submit_solution'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
]
