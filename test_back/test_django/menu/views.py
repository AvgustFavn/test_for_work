from django.shortcuts import render
from menu.dbback import status_menu


def index(req):
    return render(req, 'index.html', context={'menu': str(status_menu())})

def dog(req):
    return render(req, 'dog.html', context={'menu': status_menu()})

def food(req):
    return render(req, 'food.html', context={'open': True, 'open_too': True, 'menu': status_menu()})

def fry(req):
    return render(req, 'fry.html', context={'open': True, 'open_too': True, 'menu': status_menu()})

def ice(req):
    return render(req, 'ice_cream.html', context={'open': True, 'open_too': True, 'menu': status_menu()})

def potato(req):
    return render(req, 'potato.html', context={'open': True, 'open_too': True, 'menu': status_menu()})
