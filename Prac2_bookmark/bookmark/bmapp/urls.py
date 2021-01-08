from django.urls import path
from .views import BookmarkListView, BookmarkCreateView, BookmarkDetailView, BookmarkUpdateView, BookmarkDeleteView
#위의 뷰 import가 너무 길어지면 => from .views import *

#함수형 뷰(from 앱이름.views import~ 한 경우)는 path에 뷰이름만 써주면 되지만,
#class형 뷰일땐 .as_view()를 붙여줘야 정상작동.
urlpatterns=[
    path('',BookmarkListView.as_view(), name='list'),   #name을 가지고 해당 url패턴을 찾을 수 있도록 함.
    path('create/',BookmarkCreateView.as_view(), name='create'),
    path('detail/<int:pk>/', BookmarkDetailView.as_view(),name='detail'),
    path('update/<int:pk>', BookmarkUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', BookmarkDeleteView.as_view(), name='delete'),
]