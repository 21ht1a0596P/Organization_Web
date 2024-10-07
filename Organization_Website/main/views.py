from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def events(request):
    return render(request, 'events.html')

def placements(request):
    return render(request, 'placements.html')

def materials(request):
    return render(request, 'materials.html')

def results(request):
    return render(request, 'results.html')
