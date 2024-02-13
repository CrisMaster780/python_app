from django.shortcuts import render

def home_index(request):
    template = 'home.html'
    context = {
        'titulo': 'Sistema '
    }
    
    return render(request, template, context)