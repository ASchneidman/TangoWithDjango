from django.shortcuts import render, HttpResponse

def index(request):
        context_dict = {'boldmessage':"Crunchy, creamy, cookie, cupcake!"}

        return render(request, 'rango/index.html', context=context_dict)

def about(request):
        context_dict = {'00'}
        return render(request, 'rango/about.html', context=context_dict)
