

from django.db import models

class Question(models.Model):

    text_question = models.CharField(max_length=200)
    date = models.DateTimeField("Date")

    def __str__(self):
        return self.text_question


class Choice(models.Model):

    text_choice = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.text_choice
