from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'myapp/index.html')


def dashboard(request):
    return render(request,'myapp/dash_board.html')