from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader

# Create your views here.
from .models import Question

from django.http.response import HttpResponseRedirect
from django.urls.base import reverse
from django.views import generic

from django.utils import timezone
from django.db.models import Count

## A ListView abstracts the concept of "display a list of objects"
## A DetailView abscracts the concept of "show the details of a particular type of object"
## DetailView.context_object_name not necessary when DetailView.model provided and the default is ok


## index view as generic view (class based)
class IndexView(generic.ListView):
    template_name = "poll/index.html"
    context_object_name = "latest_question_list"
    
    def get_queryset(self):
        """
        questions that are in the past and have at least 1 choice
        """
        return Question.objects.filter(
            pub_date__lte = timezone.now()
        ).annotate(
            Count("choice")
        ).filter(
            choice__count__gt = 0
        ).order_by("-pub_date")[:5]


## detail view as generic view (class based)
class DetailView(generic.DetailView):
    model = Question
    template_name = "poll/detail.html"

    def get_queryset(self):
        """
        questions that are in the past and have at least 1 choice
        """
        return Question.objects.filter(
            pub_date__lte = timezone.now()
        ).annotate(
            Count("choice")
        ).filter(
            choice__count__gt = 0
        )

## results view as a generic view (class based)
class ResultsView(generic.DetailView):
    model = Question
    template_name = "poll/results.html"

    def get_queryset(self):
        """
        questions that are in the past and have at least 1 choice
        """
        return Question.objects.filter(
            pub_date__lte = timezone.now()
        ).annotate(
            Count("choice")
        ).filter(
            choice__count__gt = 0
        )

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # redisplay the question voting form
        render(request, "poll/detail.html", {
            "question": question,
            "error_message": "Choose your vote!"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being POSTed twice if a
        # user hits the Back button
        return HttpResponseRedirect(reverse("poll:results", args=(question.id,)))
