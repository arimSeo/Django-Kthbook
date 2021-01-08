from django.db import models
from django.urls import reverse   

# models.Model을 상속받는 클래스:Bookmark
# 두개의 클래스 변수(=필드): site_name, url 
class Bookmark(models.Model):
    site_name= models.CharField(max_length=100)
    url= models.URLField('Site URL')    #'site URL'기본 있는 속성값?????
    
    #관리자 페이지에 object(번호) 식으로 보이는 것을 원하는 목록내용형태로 변경하기.
    #__str__메서드(함수): return값이 항상 문자열
    def __str__(self):
        return "이름: " + self.site_name + ", 주소 : " + self.url
        #객체를 출력할때 나타날 값.

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])
    #get_absolute_url :객체의 상세화면 주소를 return.
    #reverse메소드 : urlpattern의 이름과 추가 인자를 전달받아 url을 생성하는 method