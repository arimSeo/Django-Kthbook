from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from .models import Question, Choice    #모델 import

def index(request):
    #index view요청이 오면 역순(-)으로 5개 까지만 정렬하고 latest_question_list에 저장
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'index.html', context)

def detail(request, question_id):
    #  get_object_or_404로 해당 Question 모델을 찾고, 템플릿으로 전해주고있다.
    question= get_object_or_404(Question, pk=question_id)
    return render(request, 'detail.html', {'question': question})

def result(request,question_id):
    question= get_object_or_404(Question, pk=question_id)
    return render(request,'result.html',{'question':question})

def vote(request, question_id):
    question=get_object_or_404(Question,pk=question_id)
    try:
        #request.POST['변수이름']: 전달받은 변수의 값들을 확인 할 수 있다.
        # html form에서 post요청-> get(): ()안 조건 받아와-> post로 넘어온 choice값으로 선택된 항목(choice)을 넣기
        selected_choice= question.choice_set.get(pk=request.POST['choice']) #(detail.html에 choice변수)
    #예외가 발생했을 시에 question 모델과 에러 메세지를 template에 전달
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'detail.html',{'question':question, 'error_message':"쉣",})
    else:
        # choice를 잘 얻어왔으면 투표 수를 1증가-> result창으로 이동
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('myapp:result', args=(question.id,)))