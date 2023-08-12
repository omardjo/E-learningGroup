from django.shortcuts import render

# Create your views here.

# niveaux_api/views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Module
from .serializers import ModuleSerializer
from rest_framework import status

@api_view(['GET'])
def get_module(request, pk):
    try:
        module = Module.objects.get(pk=pk)
    except Module.DoesNotExist:
        return Response({'error': 'Module not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ModuleSerializer(module)
    return Response(serializer.data)

@api_view(['PUT'])
def update_module(request, pk):
    try:
        module = Module.objects.get(pk=pk)
    except Module.DoesNotExist:
        return Response({'error': 'Module not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ModuleSerializer(module, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_module(request, pk):
    try:
        module = Module.objects.get(pk=pk)
    except Module.DoesNotExist:
        return Response({'error': 'Module not found'}, status=status.HTTP_404_NOT_FOUND)

    module.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def list_modules(request):
    modules = Module.objects.all()
    serializer = ModuleSerializer(modules, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_module(request):
    serializer = ModuleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)