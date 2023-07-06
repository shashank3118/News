from django.shortcuts import render


def homepage(request):
    return render(request,"front-end/index.html",{"nbar":"home"})

def PoliticsView(request):
    return render(request,"front-end/politics.html", {"nbar":"politics"})

def single_news(request):
    return render(request,"front-end/education.html" , {"nbar":"edu"})

def single2_news(request):
    return render(request,"front-end/city.html" ,  {"nbar":"city"})

def single3_news(request):
    return render(request,"front-end/features.html" , {"nbar":"feat"})

def contact(request):
    return render(request,"front-end/contact.html", {"nbar":"contact"})