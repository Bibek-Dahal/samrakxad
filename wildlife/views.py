
from django.shortcuts import render
from django.views import View
from .imageclassifier import testModel
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
from .file_upload import upload_file
from django.conf import settings

from .image_detection import run_detector

# Create your views here.
class ImageUploadView(View):
    def get(self,request):
        print(settings.MODULE_HANDLE)
        return render(request,'wildlife/home.html')
    
    def post(self,request):
        if not request.FILES.get('animal'):
            context = {'validation_error':'Image is required'}
            return render(request,'wildlife/home.html',context)
        
        testModel(request.FILES.get('animal'))
        return HttpResponseRedirect(reverse_lazy('wildlife:homepage'))

class RunDetector(View):
    def get(self,request):
        pass