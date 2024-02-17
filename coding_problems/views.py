from django.shortcuts import render, redirect
from .models import Problem, Solution
from django.contrib.auth import authenticate, login
from .forms import RegistrationForm
from django.contrib.auth.views import LogoutView



class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        # Call Django's logout function to log out the user
        from django.contrib.auth import logout
        logout(request)
        # Redirect to the homepage or any other page you want
        return redirect('/')

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to login page or another page
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})




def home(request):
    return redirect('list_problems')

def list_problems(request):
    problems = Problem.objects.all()
    return render(request, 'coding_problems/list_problems.html', {'problems': problems})

def show_problem(request, problem_id):
    problem = Problem.objects.get(id=problem_id)
    return render(request, 'coding_problems/show_problem.html', {'problem': problem})

def submit_solution(request, problem_id):
    if request.method == 'POST':
        return redirect('leaderboard')
    else:
        return render(request, 'coding_problems/show_problem.html', {'problem_id': problem_id})

def leaderboard(request):
    solutions = Solution.objects.order_by('-submitted_at')[:10]
    return render(request, 'coding_problems/leaderboard.html', {'solutions': solutions})
