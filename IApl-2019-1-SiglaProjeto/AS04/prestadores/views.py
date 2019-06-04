from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. Você está na view index")

def criar(request):
    return HttpResponse("Tela de criação de prestadores")