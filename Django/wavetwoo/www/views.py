from django.shortcuts import render, redirect

# Create your views here.
def index(request):

    urls = [
        'snap_history',
        'cooktea_home',
    ]

    return redirect(urls[1])
