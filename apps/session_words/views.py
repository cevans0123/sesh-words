from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
# Create your views here.

def index(request):
    if 'words' not in request.session:
        request.session['words'] = []
    context = {
        'time': strftime("%I:%M:%S%p, %B %d, %Y", gmtime()),
    }
    
    return render(request, 'session_words/index.html', context)
def submit(request):
    if 'big_font' in request.POST:
        showbig = "big"
    else:
        showbig = 0
    if 'color' in request.POST:
        color = request.POST['color']
    else:
        color = 'black' 
    new_dictionary = { 
        'words': request.POST['words'],
        'color': color,
        'show_big': showbig,
    }
    request.session['words'].append(new_dictionary)
    request.session.modified = True
    
    return redirect("/")
    

def clear (request):
    request.session['words'] = []
        
    return redirect("/")

