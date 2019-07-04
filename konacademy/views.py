from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import viewsets
from .models import KonUser
from rest_framework.permissions import IsAuthenticated
from .serializers import AssetPackageSerializer, LessonSerializer
from rest_framework import generics
from .models import KonUser, AssetPackage, Lesson
# Create your views here.
# ViewSets define the view behavior.
class AssetPackageView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    parser_classes = (MultiPartParser, FormParser)
    queryset = AssetPackage.objects.all()
    serializer_class = AssetPackageSerializer

    def perform_create(self, serializer):
        print (self.request.user)
        serializer.save(author=self.request.user)

class AssetPackageDetailView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    parser_classes = (MultiPartParser, FormParser)
    queryset = AssetPackage.objects.all()
   
    serializer_class = AssetPackageSerializer
    
   