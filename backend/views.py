import logging
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.template import loader
from . import models

# Create your views here.

def index(request):
    last_question_list = models.Question.objects.order_by("published_date")
    context = {
        "last_question_list": last_question_list,
    }
    return render(request, 'backend/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(models.Question, pk=question_id)
    return render(request, 'backend/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):    
    return HttpResponse("You're voting on question %s." % question_id)