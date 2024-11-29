from django.http import HttpResponse
from django.shortcuts import render


# views  controller hota hai django me


def homePage(request):
    data = {
        "title": "Home Page",
        "bddata": "We will Coming Soon with Best Version Of Myself",
    }
    return render(request, "index.html", data)


def aboutUs(request):
    return HttpResponse("Welcome To New Project")


def course(request):
    return HttpResponse("Welcome To New Course")


def billu(request):
    return render(request, "billu.html")


def courseDetails(request, courseid):
    return HttpResponse(courseid)
