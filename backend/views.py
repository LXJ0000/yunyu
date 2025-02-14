from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from . import models


# Create your views here.

class IndexView(generic.ListView):
    template_name = 'backend/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return models.Question.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:5]


class DetailView(generic.DetailView):
    model = models.Question
    template_name = 'backend/detail.html'

    def get_queryset(self):
        return models.Question.objects.filter(published_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = models.Question
    template_name = 'backend/results.html'


def vote(request, question_id):
    question = get_object_or_404(models.Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, models.Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'backend/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('backend:results', args=(question_id,)))
