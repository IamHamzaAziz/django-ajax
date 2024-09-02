from django.shortcuts import render, HttpResponse
from .models import Item
import json

# Create your views here.
def add_item(request):
    if request.method == 'POST':
        name = request.POST['name']
        if name:
            item = Item(name=name)
            item.save()
            return HttpResponse(json.dumps({ 'name': item.name}), content_type='application/json')
        
    return HttpResponse(json.dumps({ 'error': 'Invalid request'}), content_type='application/json')

def index(request):
    return render(request, 'index.html')

def getItems(request):
    items = Item.objects.all()
    items_list = [{'name': item.name} for item in items]
    return HttpResponse(json.dumps({'items': items_list}), content_type='application/json')

