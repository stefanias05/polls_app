
# Create your views here.

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Choice, Question
from django.template import loader
from django.urls import reverse



def index(request):
    """
    last questions
    :param request:
    :return:
    """
    latest_question = Question.objects.order_by("date")[::-1]
    template = loader.get_template("index.html")
    # output = ", ".join([q.text_question for q in latest_question])
    context = {
        'latest_question': latest_question,
    }
    return HttpResponse(template.render(context, request))
    # return render(request, 'index.html', context)


# def HTTP404():
#     text ="Question does not exist"
#     return text


def details(request, question_id):

    question = get_object_or_404(Question, pk=question_id)
    # context = {
    #     'question': question
    # }
    return render(request, 'detail.html', {'question': question})



def results(request, question_id):
    question = get_object_or_404(Question, pk= question_id)
    return render(request, 'results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk= request.POST['choice'])
        # context = {
        #     "question": question,
        #     "error_message": "You didn't select a choice!",
        # }
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'detail.html', {
                "question": question,
                "error_message": "You didn't select a choice.",
            })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

