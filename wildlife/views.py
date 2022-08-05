import io
import re
from django.shortcuts import render
from django.views import View
from .imageclassifier import testModel
import os
# Create your views here.
class ImageUploadView(View):
    def get(self,request):
        print(f"{os.getcwd()}/wildlife/seqmodel/wildlife_monitoring.h5")
        return render(request,'wildlife/home.html')
    
    def post(self,request):
        print(request.FILES.get('animal'))
        print(type(request.FILES.get('animal')))
        if not request.FILES.get('animal'):
            context = {'validation_error':'Image is required'}
            return render(request,'wildlife/home.html',context)
        image_path = request.FILES.get('animal')
        testModel(image_path)
        return render(request,'wildlife/home.html')