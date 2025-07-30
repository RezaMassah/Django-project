from django.shortcuts import render

def home(request):
    return render(request, 'myapp1/main.html')
