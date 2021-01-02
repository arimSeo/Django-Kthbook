from django.urls import path
from .views import detail,index, result,vote

app_name= 'myapp'

urlpatterns = [
    path('',index, name='index'),
    path('detail/<int:question_id>',detail, name='detail'),
    path('result/<int:question_id>',result, name='result'),     #<>는 변수의미
    path('vote/<int:question_id>',vote, name='vote'),
]
