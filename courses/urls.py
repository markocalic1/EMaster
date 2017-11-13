from django.conf.urls import url
from . import views

app_name = 'courses'

urlpatterns = [
    url(r'^$' ,views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    #Course urls
    url(r'^add/$', views.CourseCreate.as_view(), name='course-add'),

    url(r'^(?P<pk>[0-9]+)/chapter/update/$', views.CourseUpdate.as_view(), name='course-update'),

    url(r'^(?P<pk>[0-9]+)/chapter/delete/$', views.CourseDelete.as_view(), name='course-delete'),

    url(r'^(?P<pk>[0-9]+)/chapter/add/$', views.ChapterCreate.as_view(), name='chapter-add'),
    url(r'^(?P<course_pk>[0-9]+)/chapter/(?P<pk>[0-9]+)/$', views.ChapterView.as_view(), name='chapter-detail'),

    url(r'^(?P<course_pk>[0-9]+)/chapter/(?P<chapter_pk>[0-9]+)/block/text/add$', views.TextBlockCreate.as_view(), name='text-add'),
    url(r'^(?P<course_pk>[0-9]+)/chapter/(?P<chapter_pk>[0-9]+)/block/video/add$', views.AddVideoBlock.as_view(), name='video-add'),
    url(r'^(?P<course_pk>[0-9]+)/chapter/(?P<chapter_pk>[0-9]+)/block/images/add$', views.AddImageBlock.as_view(),name='images-add'),
    url(r'^(?P<course_pk>[0-9]+)/chapter/(?P<chapter_pk>[0-9]+)/block/quiz/add$', views.QuizCreate.as_view(), name='quiz-add'),
]
