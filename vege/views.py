from django.shortcuts import render, redirect
from .models import *
from django.core.files.images import ImageFile
from django.http import HttpResponse


def receipe(request):
    if request.method == "POST":
        receipe_image = request.FILES.get("receipe_image")
        receipe_name = request.POST.get("receipe_name")
        receipe_description = request.POST.get("receipe_description")

        print(receipe_name)
        print(receipe_description)
        print(receipe_image)

        image_file = ImageFile(receipe_image)

        recipe = Receipe.objects.create(
            receipe_name=receipe_name,
            receipe_description=receipe_description,
            receipe_image=image_file,
        )
        return redirect("/receipe")
    
    queryset = Receipe.objects.all()
    
    # if request.GET.get('search'):
    #     queryset = queryset.filter(receipe_name__icontains = request.GET.get('search'))
    
    if request.GET.get('search'):
        search_term = request.GET.get('search')
        queryset = queryset.filter(receipe_name__icontains=search_term)
        
        
    context = {'receipes': queryset}

    return render(request, "receipe.html",context)


def delete_receipe(request,id):
    print(id)
    
    queryset = Receipe.objects.get(id = id)
    queryset.delete()
    return redirect("/receipe/")

def update_receipe(request,id):
    queryset = Receipe.objects.get(id = id)
    if request.method == "POST":
        receipe_name = request.POST.get("receipe_name")
        receipe_description = request.POST.get("receipe_description")
        receipe_image = request.FILES.get("receipe_image")
        
      
        queryset.receipe_name = receipe_name
        queryset.receipe_description = receipe_description

        if receipe_image:
            queryset.receipe_image = receipe_image
         
        queryset.save()    
        return redirect("/receipe/")
    
 
    context = {'receipe': queryset}
    return render(request, "update_receipe.html",context)