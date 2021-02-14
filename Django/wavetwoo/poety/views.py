from django.shortcuts import render, redirect

from .models import SnapPoety, SnapHistory


# Create your views here.
def poety_menu(request):

    snap_histories = SnapHistory.objects.order_by('date', 'name')

    context = {
        'snap_histories': snap_histories,
    }

    return render(request, 'poety/poety_menu.html.django', context)


def snap_history(request, slug):

    history = SnapHistory.objects.filter(slug=slug).first()
    snaps = SnapPoety.objects.filter(history=history).order_by('date', 'id').all()

    context = {
        'history': history,
        'snaps': snaps,
    }

    return render(request, 'poety/snap_history.html.django', context)
