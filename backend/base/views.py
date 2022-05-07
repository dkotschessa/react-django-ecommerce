from django.shortcuts import render
from django.http import JsonResponse
from .products import products
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


@api_view(["GET"])
def getRoutes(request):
    routes = [
        "/api/products/",
        "/api/products/crate",
        "/api/products/upload",
        "/api/produts/<id>/reviews/",
        "/api/products/top/",
        "/api/products/<id>/",
        "/api/products/delte/<id>",
        "/api/products/<update>/<id>",
    ]

    return Response(routes)


@api_view(["GET"])
def getProducts(request, pk):
    product = None
    for i in products:
        if i["_id"] == pk:
            product = i
            break
    return Response(product)
