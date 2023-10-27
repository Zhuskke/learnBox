from django.shortcuts import render

def home(request):
    return render(request, "home1.html", {})

def learner_view_profile(request):
    return render(request, 'learner_template/learner_view_profile.html', {})
def dashboard(request):
    return render(request, 'dashboard.html', {})

def announcement(request):
    return render(request, 'announcement.html', {})

def activities(request):
    return render(request, 'activities.html', {})

def calendar(request):
    return render(request, 'calendar.html', {})