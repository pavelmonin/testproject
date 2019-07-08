from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import Pict

# galleryC = [
#         {
#             'comment': 'Our first record',        
#             'date' : '1 January',
#             'picture': 'George'
#         },

#          {
#             'comment': 'Our first record',        
#             'date' : '1 January',
#             'picture': 'George'
#         },

#          {
#             'comment': 'Our first record',        
#             'date' : '1 January',
#             'picture': 'George'
#         },

# ]

def home(request):
    # data = {
    #             'galleryC': galleryC ,
    #             'title':'Main page (from home)'
    #     }

    if request.method == 'GET': 
  
        # getting all the objects of hotel. 
        galleryC = Pict.objects.all()  
        return render(request, 'gallery/home.html', {'galleryC' : galleryC}) 

    # return render(request,'gallery/home.html', data)


def upload(request):
    if request.method == 'POST': 
        form = PictForm(request.POST, request.FILES) 
  
        if form.is_valid(): 
            form.save() 
            return redirect('success') 
    else: 
        form = PictForm() 
    return render(request, 'gallery/upload.html', {'form' : form}) 

    
  
  
def success(request): 
    return HttpResponse('successfuly uploaded') 
    # return render(request,'gallery/upload.html')    
