# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Context, loader
from play.models import Question

def index(request):
    question_list = Question.objects.all().order_by('-paper')[:5]
    return render_to_response('play/index.html', {'question_list': question_list})

def play(request, play_id):
    p = Question.objects.get(id = play_id)
    return render_to_response('play/play.html', {'question': p})