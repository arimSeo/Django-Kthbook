# from django.shortcuts import render   -> 함수형 뷰일때 사용하므로 제거해도 ok!
from .models import Bookmark
    #generic(클래스형)뷰 사용
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy    #reverse_lazy는 reverse와 같은 기능인데 generic view에서 주로 사용한다.
    #타이밍 로딩 문제로 generic view에서는 reverse는 사용할 수 없고 reverse_lazy를 사용해야한다.
from django.views.generic.detail import DetailView

#북마크 목록
class BookmarkListView(ListView):
    model= Bookmark     # models.py의 Bookmark모델 설정
    template_name='bookmark_list.html'
    paginate_by= 5

#북마크 추가하기
class BookmarkCreateView(CreateView):
    model= Bookmark
    template_name='create.html'
    template_name_suffix= '_create'    #???? 템플릿 접미사 (보통 모델명_xxx)-> bookmark_create.html이 템플릿이 된다는 뜻

    fields=['site_name','url']       # models.py에서 가져온 필드들(fields변수= 어떤 필드들을 입력받을 것인지.)
    success_url= reverse_lazy('list')
     #success_url은 글쓰기를 완료하고 이동할 페이지(url name으로) 설정

#북마크 상세
class BookmarkDetailView(DetailView):
    model=Bookmark
    template_name='detail.html'

#북마크 수정
class BookmarkUpdateView(UpdateView):
    model=Bookmark
    template_name='update.html'
    fields=['site_name','url']
    template_name_suffix='_update'

class BookmarkDeleteView(DeleteView):
    model= Bookmark
    template_name='delete.html'
    success_url= reverse_lazy('list')






#함수형

#북마크 목록
# def book_list(request):
#     return render(request,'bookmark_list.html')

