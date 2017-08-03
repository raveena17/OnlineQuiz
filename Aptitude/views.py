from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.db import IntegrityError
from .models import Attendee, Question, Choice
from django.utils import timezone
from django.views import generic
from django.shortcuts import redirect
import datetime


def view_homepage(request):
    return render(request, 'home.html')

def attendee_register(request):
    return render(request,'register_form.html')

def save_attendee_details(request):
    # import pdb;pdb.set_trace()
    attendee = Attendee(
        name = request.POST.get('name'),
        qualification = request.POST.get('qualification'),
        age = request.POST.get('age'),
        phoneNo = request.POST.get('phoneNo'),
        mailId = request.POST.get('mailId'),
        address = request.POST.get('address'),
        date_of_birth = request.POST.get('date_of_birth'),
        gender = request.POST.get('gender'),
        language = request.POST.get('language')
        )
    attendee.save()
    return render(request, 'language.html', {'attendee': attendee})

def add_attendee(request):
    attendee = save_attendee_details(request)
    result = Result(attendee = attendee, marks = 0)
    result.save()
    return render(request, 'Aptitude/language')

def view_attendee_list(request):
    postlist = Attendee.objects.all()
    context = {'postlist': postlist}
    return render(request, 'attendee_details.html',{'postlist':postlist})

def delete_attendee(request):
    _id = request.GET['id']
    attendee = Attendee.objects.get(pk = _id)
    attendee.delete()
    return HttpResponse(attendee.name +"   "+"record deleted")

class PythonQuestionView(generic.ListView):                
    template_name = 'index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(subject='Python')
         # return Question.objects.filter()[:10] 

class JavaQuestionView(generic.ListView):                
    template_name = 'index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(subject='Java')
        # return Question.objects.filter()[11:15] 
       
class QuestionDetailView(generic.DetailView):
    model = Question
    template_name = 'question.html'


# def scores_update(request, id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         return render(request, 'question.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         # call --- scores_update(attendee_id, question_id, answer)

# def scores_update(attendee_id, question_id, answer):
#     '''validate attendee answer is correct or not'''
#     question = get_object_or_404(Question, pk=question_id)
#     ans=question.answer_text
#     choice = request.POST.get('choice')
#     if str(ans.answer_text) == str(answer):
#         result = Result.objects.filter(attendee=attendee_id)
#         result.update(marks=result.marks+1)
#         return render(request,'result.html')

