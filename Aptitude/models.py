from __future__ import unicode_literals
from django.db import models
import datetime
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone



class Attendee(models.Model):
	name = models.CharField(max_length=200)
	qualification = models.CharField(max_length=200)
	age = models.IntegerField()
	phoneNo = models.IntegerField(unique=True)
	mailId = models.EmailField(max_length=200, unique=True)
	address = models.CharField(max_length=200)
	date_of_birth = models.DateField()
	gender = models.CharField(max_length=200)
	language = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Question(models.Model):
    subject = models.CharField(max_length=200)
    question_text = models.CharField(max_length=200)
    answer_text= models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.subject

    # def was_published_recently(self):
    #     now = timezone.now()
    #     return now - datetime.timedelta(days=1) <= self.pub_date <= now
    # was_published_recently.admin_order_field = 'pub_date'
    # was_published_recently.boolean = True
    # was_published_recently.short_description = 'published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=120)

    def __str__(self):
        return self.choice_text

class Result(models.Model):
    attendee = models.ForeignKey(Attendee, on_delete=models.CASCADE)
    marks = models.IntegerField(default=0)

    def __str__(self):
        return self.attendee

