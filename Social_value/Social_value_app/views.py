from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Question
# Create your views here.

class QuestionsView(ListView):
    model =  Question
    template_name = 'question_list.html'
    context_object_name = 'questions'