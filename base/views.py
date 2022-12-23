from django.shortcuts import render

def HomeView(request, *args, **kwargs):
    template = "home.html"
    context = {

    }

    return render(request, template, context)