from django.contrib import admin

#모델 추가할때마다 admin에 추가!!!
from .models import Question, Choice
#관리자페이지 폼 customizing 이전
# admin.site.register(Question)
# admin.site.register(Choice)

# 관리자페이지 customizing
# fieldsets변수를 이용해 입력/수정 화면에서 각 항목들을 그룹화 하고 그룹의 이름까지 설정할 수 있다.
# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets=[
#         (None, {'fields':['question_text']}),
#         ('Date information',{'fields':['pub_date']}),
#     ]

# admin.site.register(Question, QuestionAdmin)

# 답변까지 같이 등록/수정 한번에 추가 가능하게
    #Choice모델을 위한 옵션 클래스 
class ChoiceInline(admin.StackedInline):
    model=Choice
    extra=3     #여분 choice항목 3개까지 추가할 수 있게 빈칸

class QuestionAdmin(admin.ModelAdmin):
    fieldsets=[
        (None, {'fields':['question_text']}),
        ('Date information',{'fields':['pub_date']}),
    ]
    inlines=[ChoiceInline]

admin.site.register(Question, QuestionAdmin)    #admin페이지에 ()안 항목들이 등록되도록

