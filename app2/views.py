from django.shortcuts import render

# Create your views here.
def app2_fun2(request):
    return render(request,'app2/first.html')