from django.shortcuts import render, redirect
from .models import Problem, Solution


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
