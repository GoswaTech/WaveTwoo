from django.shortcuts import render, redirect

from .models import SnapPoety


# Create your views here.
def snap_history(request):

    snaps = SnapPoety.objects.order_by('date', 'id').all()

    context = {
        'snaps': snaps,
    }

    return render(request, 'poety/snap_history.html.django', context)
