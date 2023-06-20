from django.shortcuts import render

from django.http import HttpResponse 

def home(request):
    
    peoples = [
        {
            'name':"khan" ,'age':24
        },
        {
            'name':"pasha" ,'age':25
        },
        {
            'name':"ayub" ,'age':15
        },
    ]
    
    text = '''
    Lorem ipsum dolor sit amet consectetur adipisicing elit. Ab voluptatibus et quos unde quasi earum temporibus necessitatibus, quibusdam aliquam dolore beatae commodi magnam sapiente mollitia animi quas fugiat cumque maxime.
    '''
    
    vegetables = ['pumpkin','potato','beans','tomato']
    
    return render(request, "home/index.html", context = {"people" : peoples ,"text":text, "vegetables":vegetables,"page":"Django Learning 2023"})   #Bydefault it will understand template file


def about(request):
    context = {'page':'about'}
    return render(request, "home/about.html",context)

def contact(request):
    context = {'page':'contact'}
    return render(request, "home/contact.html",context)


def success_page(request):
    print("*" * 10)
    return HttpResponse("<h1>Hey this is a Success Page</h1>")









# def home(request):
#     return HttpResponse("""<h1>Hey I am a Django Server.</h1>
#                         <P>This is a Paragraph Tag</P>
#                         """)


#  for people in peoples:
#         print(people)