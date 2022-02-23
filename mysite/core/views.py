from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
import os



def upload(request):
    context = {}
    if request.method == 'POST':
        try:
            uploaded_file = request.FILES['document']
            file_size=uploaded_file.size
            # fs = FileSystemStorage()
            # name = fs.save(uploaded_file.name, uploaded_file)
            context['url'] = 'succesfully'
            context['file_size'] = file_size
        except:
            pass
    return render(request, 'upload.html', context)

