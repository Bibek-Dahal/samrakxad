from django.shortcuts import render
from django.views import View
from django.http.response import HttpResponseRedirect
from .file_upload import upload_file
import os
from django.core.files.storage import FileSystemStorage
from .imageclassifier import disp_image


# Create your views here.
class ImageUploadView(View):
    def get(self,request):

        return render(request,'wildlife/home.html')
    
    def post(self,request):
        if not request.FILES.get('animal'):
            context = {'validation_error':'Image is required'}
            return render(request,'wildlife/home.html',context)
        file_url = upload_file(request.FILES.get('animal'))
        result = disp_image(file_url)
   
        list_of_names = []
        FileSystemStorage().delete(file_url)
        for r in result:
            for k in r:
                percentage_list = list(k)
               
                list_of_names.append({
                    'name':percentage_list[1],
                    'percentage':round(percentage_list[2]*100,2)
                })

        return render(request,'wildlife/home.html',{'list_of_names':list_of_names})

class RunDetector(View):
    def post(self,request):
        image = request.FILES.get('animal')
        file_url = upload_file(image)

        FileSystemStorage().delete(f"{os.getcwd()}{file_url}")
        return HttpResponseRedirect('/')