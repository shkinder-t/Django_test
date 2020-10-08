from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import forms
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from tania_proect.member.models import NewCreationForm


class CreateUserView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('polls:index')
    template_name = 'member/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context['form'].errors,'context')
        return context

    def post(self, request, *args, **kwargs):
        res = super().post(request, *args, **kwargs)
        if self.object:
            login(user=self.object, request=request)
            print(self.object)
        # form_kwargs = self.get_form_kwargs()
        # username = form_kwargs['data']['username']
        # user = User.objects.get(username=username)
        # login(user=user, request=request)
        return res


class Newview(CreateView):
    form_class = NewCreationForm
    success_url = reverse_lazy('polls:index')
    template_name = 'member/index2.html'
