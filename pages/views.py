from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "home.html", {})

def about(request):
    return render(request, "about.html", {})

def education(request):
    return render(request, "education.html", {})

def health(request):
    return render(request, "health.html", {})

def empowerment(request):
    return render(request, "empowerment.html", {})

def school(request):
    return render(request, "school.html", {})

def volunteers(request):
    return render(request, "volunteers.html", {})

def work(request):
    return render(request, "work.html", {})

def contact(request):
    return render(request, "contact.html", {})

def faq(request):
    return render(request, "faq.html", {})