from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Quiz

class IndexView(generic.ListView):
    template_name = "index.html"
    context_object_name = "all_quizs"

    def get_queryset(self):
        return Quiz.objects.all()

class DetailView(generic.DetailView):
    model = Quiz
    template_name = "detail.html"

class QuizCreate(CreateView):
    model = Quiz
    fields = ['quizTitle','author','matter']

class QuizUpdate(UpdateView):
    model = Quiz
    fields = ['quizTitle','author','matter']

class QuizDelete(DeleteView):
    model = Quiz
    success_url = reverse_lazy('index')
