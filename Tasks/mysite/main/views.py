from django.http import JsonResponse, Http404
from django.shortcuts import get_object_or_404
from .models import Author, Book, Publisher, Store, Customer, Order, OrderItem, Review

def get_model_by_id(request, model_name, object_id):
    models = {
        'author': Author,
        'book': Book,
        'publisher': Publisher,
        'store': Store,
        'customer': Customer,
        'order': Order,
        'orderitem': OrderItem,
        'review': Review,
    }

    model = models.get(model_name.lower())
    if not model:
        return JsonResponse({'error': 'Invalid model name'}, status=400)

    try:
        obj = get_object_or_404(model, id=object_id)
        data = {field.name: getattr(obj, field.name) for field in model._meta.fields}
        return JsonResponse(data)
    except Http404:
        return JsonResponse({'error': f'{model_name} with id {object_id} not found'}, status=404)
