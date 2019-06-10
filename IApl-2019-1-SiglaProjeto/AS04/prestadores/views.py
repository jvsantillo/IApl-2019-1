from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. Index view")

def person (request, person_id):
    return HttpResponse("You are looking at person %s" % person_id)
def create_person(request):
    return HttpResponse("In development... You are creating a person")
def update_person(request, person_id):
    return HttpResponse("In development... You are updating person ID %s." % person_id)
def delete_person(request, person_id):
    return HttpResponse("In development... You are deleting person ID %s." % person_id)
def retrieve_persons(request):
    return HttpResponse("In development...Here are all persons")

def supplier (request, supplier_id):
    return HttpResponse("You are looking at supplier %s" % supplier_id)
def create_supplier(request):
    return HttpResponse("In development... You are creating a supplier")
def update_supplier(request, supplier_id):
    return HttpResponse("In development... You are updating supplier ID %s." % supplier_id)
def delete_supplier(request, supplier_id):
    return HttpResponse("In development... You are updating supplier ID %s." % supplier_id)
    return HttpResponse("In development... You are deleting supplier ID %s." % supplier_id)
def retrieve_suppliers(request):
    return HttpResponse("In development...Here are all suppliers")

def expertise (request, expertise_id):
    return HttpResponse("You are looking at expertise %s" % expertise_id)
def create_expertise(request):
    return HttpResponse("In development... You are creating a expertise")
def update_expertise(request, expertise_id):
    return HttpResponse("In development... You are updating expertise ID %s." % expertise_id)
def delete_expertise(request, expertise_id):
    return HttpResponse("In development... You are updating expertise ID %s." % expertise_id)
    return HttpResponse("In development... You are deleting expertise ID %s." % expertise_id)
def retrieve_expertises(request):
    return HttpResponse("In development...Here are all expertises")