from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. Index view")

def create_person(request):
    return HttpResponse("In development... You are creating a person")
def update_person(request, person_id):
    return HttpResponse("In development... You are updating person ID %s." % person_id)
def delete_person(request, person_id):
    return HttpResponse("In development... You are deleting person ID %s." % person_id)
def retrive_persons(request):
    return HttpResponse("In development...Here are all persons")

def create_supplier(request):
    return HttpResponse("In development... You are creating a supplier")
def update_supplier(request, supplier_id):
    return HttpResponse("In development... You are updating supplier ID %s." % supplier_id)
def delete_supplier(request, supplier_id):
    return HttpResponse("In development... You are updating supplier ID %s." % supplier_id)
    return HttpResponse("In development... You are deleting supplier ID %s." % supplier_id)
def retrive_suppliers(request):
    return HttpResponse("In development...Here are all suppliers")

def create_expertise(request):
    return HttpResponse("In development... You are creating a expertise")
def update_expertise(request, expertise_id):
    return HttpResponse("In development... You are updating expertise ID %s." % expertise_id)
def delete_expertise(request, expertise_id):
    return HttpResponse("In development... You are updating expertise ID %s." % expertise_id)
    return HttpResponse("In development... You are deleting expertise ID %s." % expertise_id)
def retrive_expertises(request):
    return HttpResponse("In development...Here are all expertises")