from django.shortcuts import render

# Create your views here.

def buencafe(requests):
    return render(requests, 'buencafe/buencafe.html')

def history(requests):
    return render(requests, 'buencafe/history.html')

def coffee(requests):
    return render(requests, 'buencafe/coffee.html')