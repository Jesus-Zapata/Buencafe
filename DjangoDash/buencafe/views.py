from django.shortcuts import render

# Create your views here.

def buencafe(requests):
    return render(requests, 'buencafe/buencafe.html')

def history(requests):
    return render(requests, 'buencafe/history.html')

def coffee(requests):
    return render(requests, 'buencafe/coffee.html')

def team(requests):
    return render(requests, 'buencafe/team.html')

def eda(requests):
    return render(requests, 'buencafe/eda.html')

def tried(requests):
    return render(requests, 'buencafe/tried.html')

def model(requests):
    return render(requests, 'buencafe/model.html')

def neural(requests):
    return render(requests, 'buencafe/neural.html')