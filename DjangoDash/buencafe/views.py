from django.shortcuts import render

# Create your views here.

def buencafe(requests):
    return render(requests, 'buencafe/buencafe.html')