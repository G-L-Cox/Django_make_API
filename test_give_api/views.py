from django.shortcuts import render
from rest_framework import viewsets
from .models import stuff_temp
from .serializers import stuff_temp_serializers






class stuff_temp_view(viewsets.ModelViewSet):
    queryset = stuff_temp.objects.all()
    serializer_class = stuff_temp_serializers



