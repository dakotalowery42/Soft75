from django.shortcuts import render, redirect, HttpResponse
from .models import Diet, Soft75
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q

def dashboard(request):
    return render(request, 'pages/dashboard.html')


# def book_details(request, id):
#     book = Book.objects.get(id = id)
#     context = {
#         "book": book
#     } 
#     return render(request, 'pages/details.html', context)

@login_required
def Progress(request):
    book = Book.objects.all()
    context = {'books': book}
    return render(request, 'pages/Progress.html', context)

# SOFT 75 PLAN
@login_required
def Soft75Plan(request):
    if request.method == "GET":
        return render(request, 'pages/Soft75Plan.html')
    elif request.method == "POST":
        Diet = Diet.objects.all().filter(
            available_Diets=request.POST['Diet']) ##filters the database and checks if there's an entry or not
        if not Diet: ##if the name isn't in the database, go register it.
            Diet.objects.create(available_Diets=request.POST['Diet'])
            messages.success(request, 'Soft75 Diet added in the Database!')
            return redirect('dashboard')
        else: ## Otherwise print error and stay in the form view
            messages.warning(request, 'Soft75 Diet already in the database for this user.')
            return render(request, 'pages/Soft75Plan.html')

# ADD WORKOUT
@login_required
def Workout(request):
    Diets = Diet.objects.all()
    context = {'Diets': Diets}
    if request.method == 'GET':
        return render(request, 'pages/Workout.html', context)
    elif request.method == 'POST':
        Soft75 = Soft75.objects.all().filter(Workout=request.POST['Workout']).filter(Water=request.POST['Water']).filter(Skill=request.POST['Skill'])
        if not Soft75:
            Workout = request.POST['Workout']
            Water = request.POST['Water']
            Skill = request.POST['Skill']
            Soft75 = Soft75.objects.create(Workout=Workout, Water=Water, Skill=Skill(id=request.POST['Diet']))
            messages.success(request, 'Soft75 added in the Database!')
            return redirect('dashboard')
        else: ## Otherwise print error and stay in the form view
            messages.warning(request, 'Soft75 already in the database')
            return render(request, 'pages/Workout.html', context)
