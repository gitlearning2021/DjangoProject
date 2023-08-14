from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
# Create your views here.
def hello(request):
    return HttpResponse('Hellow World')

def about(request):
    return HttpResponse('This is my first django application')

class BookApiView(APIView):
    serializer_class=BookSerialzer
    def get(self,request):
        allbooks=Book.objects.all().values()
        return Response({"message":"List of books","Book List":allbooks})

    # def post(self,request):
    #     Book.objects.create(id=request.data["id"],
    #                         title=request.data["title"],
    #                         author=request.data["author"]
    #                         )
        
    #     book=Book.objects.all().filter(id=request.data["id"]).values()
    #     return Response({"message":"New Book Added","Book":book})   

    def post(self,request):
        print('Request data is :',request.data)
        serializer_obj = BookSerialzer(data=request.data)
        if(serializer_obj.is_valid()):
            Book.objects.create(id=serializer_obj.data.get("id"),
                                title=serializer_obj.data.get("title"),
                                author=serializer_obj.data.get("author")
                                )
        book=Book.objects.all().filter(id=request.data["id"]).values()
        return Response({"message":"New Book Added","Book":book})   