
from django.shortcuts import render
from django.views import View
from .imageclassifier import testModel
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy

# Create your views here.
class ImageUploadView(View):
    def get(self,request):
        
        return render(request,'wildlife/home.html')
    
    def post(self,request):
        if not request.FILES.get('animal'):
            context = {'validation_error':'Image is required'}
            return render(request,'wildlife/home.html',context)
        
        testModel(request.FILES.get('animal'))
        return HttpResponseRedirect(reverse_lazy('wildlife:homepage'))