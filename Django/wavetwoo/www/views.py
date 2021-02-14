from django.shortcuts import render, redirect

# Create your views here.
def index(request):

    urls = [
        'snap_history',
        'cooktea_home',
    ]

    context = {}

    #return redirect(urls[1])
    return render(request, 'www/index.html.django', context)
