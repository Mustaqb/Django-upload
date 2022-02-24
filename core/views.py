import imp
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
import os
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import humanbytes


@api_view(['POST'])
def upload_api(request):
    context = {}
    if request.method == 'POST':
        try:
            uploaded_file = request.FILES['document']
            file_size=uploaded_file.size
            # fs = FileSystemStorage()
            # name = fs.save(uploaded_file.name, uploaded_file)
            context['url'] = 'succesfully'
            context['file_size'] = humanbytes(int(file_size))
        except:
            pass
    return Response(context)

@api_view(['GET'])
def home(request):
    return Response({'context':'context'})

def upload(request):
    context = {}
    if request.method == 'POST':
        try:
            uploaded_file = request.FILES['document']
            file_size=uploaded_file.size
            # fs = FileSystemStorage()
            # name = fs.save(uploaded_file.name, uploaded_file)
            context['url'] = 'succesfully'
            context['file_size'] = humanbytes(int(file_size))
        except:
            pass
    return render(request, 'upload.html', context)

