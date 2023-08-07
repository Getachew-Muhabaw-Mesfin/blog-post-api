from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer

# Create your views here.
@api_view(['GET'])
def index(request):
    context ={"Success":"The setup was succesfull installed"}
    return Response(context)

@api_view(['GET'])
def getAllPosts(request):
    get_posts= Post.objects.all()
    serializer= PostSerializer(get_posts, many=True) # In order to Many fields to be serialized
    return Response(serializer.data)

@api_view(['GET','POST'])
def createNewPost(request):
    data = request.data
    serializer = PostSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"Success":"The Post is succesfully created"},status=201)
    else:
        return Response(serializer.errors, status=400)