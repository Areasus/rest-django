from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse
# from django.forms.models import model_to_dict
# Create your views here.
from products.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer
@api_view(["GET"])
def home(request,*args, **kwargs):
    # products = Product.objects.all().order_by('?').first()
    # response={
    #     'msg':"Hello i am a jason"
    # }
    # response['header']= request.header
    # return JsonResponse(data)
    # data={}
    # if products:
    # #     data['title']=products.title
    # #     data['content']=products.content
    # #     data['price']=products.price
    # return JsonResponse(data)
    products= Product.objects.first()
    print(products)
    if products:
        data_send =ProductSerializer(products).data
        print(data_send)

    return Response(data_send)