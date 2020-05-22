from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from MiniProjetDjango.models import *
from MiniProjetDjango.medicamentSerializers import *
from MiniProjetDjango.fournisseurSerializers import *


@api_view(['GET', 'POST'])
def medicament_list(request):
    """
    List all medicaments, or create a new medicament.
    """
    if (request.method == 'GET'):
        meds = Medicament.objects.all()
        serializer = medicamentSerializers(meds, many=True)
        return Response(serializer.data)

    elif (request.method == 'POST'):
        serializer = medicamentSerializers(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def medicament_detail(request, pk):
    """
    Retrieve, update or delete a medicament.
    """
    try:
        med = Medicament.objects.get(pk=pk)
    except Medicament.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if (request.method == 'GET'):
        serializer = medicamentSerializers(med)
        return Response(serializer.data)

    elif (request.method == 'PUT'):
        serializer = medicamentSerializers(med, data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif (request.method == 'DELETE'):
        med.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

######################################################################################################################

@api_view(['GET', 'POST'])
def fournisseur_list(request):
    """
    List all medicaments, or create a new medicament.
    """
    if request.method == 'GET':
        fournisseurs = Fournisseur.objects.all()
        serializer = fournisseurSerializers(fournisseurs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = fournisseurSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def fournisseur_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        fournisseur = Fournisseur.objects.get(pk=pk)
    except Fournisseur.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = fournisseurSerializers(fournisseur)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = fournisseurSerializers(fournisseur, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        fournisseur.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


