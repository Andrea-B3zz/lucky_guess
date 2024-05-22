from django.shortcuts import render

def login(request):
     return render(
          request,
          "userManagement/loginPage.html"
     )

def register(request):
     return render(
          request,
          "userManagement/registerPage.html"
     )

def personal(request):
     return render(
          request,
          "userManagement/personal.html"
     )