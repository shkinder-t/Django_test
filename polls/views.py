from datetime import datetime

from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from .models import Choice, Question, UsersChoise
from django.http import HttpResponseRedirect
from django.shortcuts import render


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_cindex': latest_question_list}
#     return render(request, 'polls/index.html', context)


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_cindex'
    queryset = Question.objects.all()

    # def get_queryset(self):
    #     """Return the last five published questions."""
    #     return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')


#
#

#
#
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


# def post_detail(request, slugok):
#     question = get_object_or_404(Question, slug=slugok)
#     return render(request, 'polls/detail.html', {'question': question})


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_choices = UsersChoise.objects.filter(choice__question=self.object)
        result = {}
        vsi = Choice.objects.filter(question_id=self.object.id)
        for choice in vsi:
            result[choice.choice_text] = 0

        for user_choice in user_choices:
            result[user_choice.choice.choice_text] += 1

        context['result'] = result
        return context


def time(priniatu):
    def we(*args, **kwargs):
        start = datetime.now()
        result = priniatu(*args, **kwargs)
        print(datetime.now() - start)
        return result
    return we


def login(zalogin):
    def user(*args, **kwargs):
        wsg = args[0]
        if wsg.user.is_authenticated:
            print(wsg.user.is_authenticated)
            result = zalogin(*args, **kwargs)
            return result
        else:
            return redirect(reverse('polls:index'))

    return user


@login
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        avalible_choices = question.choice_set.all().values_list('id', flat=True)
        answered_already = UsersChoise.objects.filter(choice_id__in=avalible_choices, user_id=request.user.id).exists()
        if answered_already:
            messages.add_message(request, messages.ERROR, 'You already vote')
            return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
        UsersChoise.objects.create(user_id=request.user.id, choice_id=selected_choice.id)
        messages.add_message(request, messages.SUCCESS, 'You just voted, thanks')

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))





class PollsCreate(CreateView):
    model = Question
    fields = ['question_text']


class PollsCreateChoice(CreateView):
    model = Choice
    fields = ['question', 'choice_text']


class Login(LoginView):
    template_name = 'polls/login.html'
