from django.shortcuts import render

# Create your views here.

def agency(request):
    return render(request, 'agency.html')


def banana(request):
    return render(request, 'banana.html')


def fast(request):
    return render(request, 'fast.html')


def funflat(request):
    return render(request, 'funflat.html')


def stand(request):
    return render(request, 'stand.html')


