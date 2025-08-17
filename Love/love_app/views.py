from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def love(request):
    return render(request,'love.html')
def love_two(request):
    return render(request,'love2.html')
def sorry_one(request):
    return render(request,'Sorry_1.html')
def sorry_two(request):
    return render(request,'sorry_2.html')
def sorry_three(request):
    return render(request,'sorry_3.html')

