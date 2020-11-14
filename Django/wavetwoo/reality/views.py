from django.shortcuts import render

from .models import Cooktsu

# Create your views here.
def cooktea_home(request):

    cooktsus = Cooktsu.objects.all()

    context = {
        'cooktsus': cooktsus,
    }

    return render(request, 'reality/cooktea_home.html.django', context)


def cooktea_cooktsu(request, id):

    cooktsu = Cooktsu.objects.filter(id=id).first()

    context = {
        'cooktsu': cooktsu,
    }

    return render(request, 'reality/cooktea_cooktsu.html.django', context)
