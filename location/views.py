from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from location import models as location_model
from location import serializers as  location_serializer

class LocationView(APIView):
    def post(self, request, *args, **kwargs):
        data = {
            'name': request.data.get('name'),
            'latitude': request.data.get('latitude'),
            'longitude': request.data.get('longitude'),
        }
        serializer = location_serializer.Location(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"id": serializer.data.get("id")}, status= status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
