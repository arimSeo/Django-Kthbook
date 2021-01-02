from django.db import models

class Question(models.Model):
    question_text= models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

# Question모델(테이블)에는 최대 길이가 200이고, character type으로 채워질 question_text필드가 있고,
# dateTime type이고 설명이 date published인 pub_date라는 필드가 있다.


class Choice(models.Model):
    question= models.ForeignKey(Question, on_delete= models.CASCADE)
    choice_text= models.CharField(max_length=200)
    votes= models.IntegerField(default=0)
    
# Choice모델에는 Question모델을 참조하는 ForeignKey가 있고, 
# 최대 길이가 200이고 character type인 choice_text필드와,
# 기본값이 0이고 integer type인 votes필드가 있다.


