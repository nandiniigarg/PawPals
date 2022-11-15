
from django.shortcuts import render



def index(request):
    return render(request, 'homepage.html')

def loginpage(request):
    # useremail = request.GET['user_email']
    # password = request.GET['user_password']
    return render(request, 'login.html')

def register(request):
    return render(request, 'signup.html')