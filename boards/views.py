from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from .models import Board

# Create your views here.


def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})


def board_topics(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404
    # Or use this
    # board = get_object_or_404(Board, pk=pk)
    return render(request, 'topics.html', {'board': board})
