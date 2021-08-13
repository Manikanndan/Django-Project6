from django.shortcuts import render

# Create your views here.
def app1_fun1(request):
    return render(request,'app1/first.html')