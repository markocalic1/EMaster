from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth import authenticate, login
from django.views import  generic
from django.views.generic import  View
from django.views import generic
from .models import Course, Chapter, Block, TextBlock, VideoBlock, ImageBlock, QuizBlock


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'courses/index.html'
    context_object_name = 'all_courses'

    def get_queryset(self):
        return Course.objects.all()

class DetailView(generic.DetailView):
    model = Course
    template_name = 'courses/detail.html'

#Course
class CourseCreate(CreateView):
    model = Course
    fields = ['name', 'logo']

    def get_success_url(self):
        return reverse_lazy('courses:detail', kwargs={'pk':self.object.id})


class CourseUpdate(UpdateView):
    model = Course
    fields = ['name', 'logo']

    def get_success_url(self):
        return reverse_lazy('courses:detail', kwargs={'pk':self.object.id})

class CourseDelete(DeleteView):
    model = Course
    success_url = reverse_lazy('courses:index')

#Chapter
class ChapterCreate(CreateView):
    model = Chapter
    fields = ['name']

    def form_valid(self,form):
        course = Course.objects.get(id = self.kwargs['pk'])
        form.instance.course=course
        return super(ChapterCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('courses:detail', kwargs={'pk':self.kwargs['pk']})

class ChapterUpdate(UpdateView):
    model = Chapter
    fields = ['name']

class ChapterDelete(DeleteView):
    model = Chapter
    success_url = reverse_lazy('courses:detail')


class ChapterView(generic.DetailView):
    model = Chapter
    template_name = 'courses/chapter_detail.html'

    def get_context_data(self, **kwargs):
        course = Course.objects.get(id=self.kwargs['course_pk'])
        # Call the base implementation first to get a context
        context = super(ChapterView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['chapter_list'] = course.chapter_set.all()
        context['course'] = course
        return context

#Lesson
class BlockCreate(CreateView):
    model = Block
    fields = ['title', 'chapter']

class BlockUpdate(UpdateView):
    model = Block
    fields = ['title', 'chapter']

class BlockDelete(UpdateView):
    model = Block
    success_url = reverse_lazy('courses:detail')


class TextBlockCreate(CreateView):
    model = TextBlock
    fields = ['title', 'text']
    template_name = 'courses/add_text.html'

class TextBlockUpdate(UpdateView):
    model = TextBlock
    fields = ['title', 'text']

class TextBlockDelete(DeleteView):
    model = TextBlock
    fields = ['title', 'text']
    success_url = reverse_lazy('courses:index')

class AddVideoBlock(CreateView):
    model = VideoBlock
    fields = ['link']
    template_name = 'courses/add_video.html'

    def form_valid(self,form):
        chapter = Chapter.objects.get(id = self.kwargs['chapter_pk'])
        form.instance.chapter = chapter
        return super(AddVideoBlock, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('courses:chapter-detail', kwargs={'course_pk':self.kwargs['course_pk'], 'pk':self.kwargs['chapter_pk']})


class UpdateVideoBlock(UpdateView):
    model = VideoBlock
    fields = ['link']
    template_name = 'courses/add_video.html'

    def form_valid(self,form):
        chapter = Chapter.objects.get(id = self.kwargs['chapter_pk'])
        form.instance.chapter = chapter
        return super(AddVideoBlock, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('courses:chapter-detail', kwargs={'course_pk':self.kwargs['course_pk'], 'pk':self.kwargs['chapter_pk']})

class DeleteVideoBlock(DeleteView):
    model = VideoBlock
    fields = ['link']
    success_url = reverse_lazy('courses:detail')

class AddImageBlock(CreateView):
    model = ImageBlock
    fields = ['image']
    template_name = 'courses/add_image.html'

    def form_valid(self,form):
        chapter = Chapter.objects.get(id = self.kwargs['chapter_pk'])
        form.instance.chapter = chapter
        return super(AddImageBlock, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('courses:chapter-detail', kwargs={'course_pk':self.kwargs['course_pk'], 'pk':self.kwargs['chapter_pk']})


class UpdateImageBlock(UpdateView):
    model = ImageBlock
    fields = ['image']
    template_name = 'courses/add_image.html'

    def form_valid(self,form):
        chapter = Chapter.objects.get(id = self.kwargs['chapter_pk'])
        form.instance.chapter = chapter
        return super(AddImageBlock, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('courses:chapter-detail', kwargs={'course_pk':self.kwargs['course_pk'], 'pk':self.kwargs['chapter_pk']})


class DeleteImageBlock(DeleteView):
    model = ImageBlock
    fields = ['image']
    success_url = reverse_lazy('courses:index')





class QuizCreate(CreateView):
    model = QuizBlock
    fields = ['question', 'answer']
    template_name = 'courses/add_quiz.html'

    def form_valid(self,form):
        chapter = Chapter.objects.get(id = self.kwargs['chapter_pk'])
        form.instance.chapter = chapter
        return super(QuizCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('courses:chapter-detail', kwargs={'course_pk':self.kwargs['course_pk'], 'pk':self.kwargs['chapter_pk']})

class QuizUpdate(UpdateView):
    model = QuizBlock
    fields = ['question', 'answer']

class QuizDelete(DeleteView):
    model = QuizBlock
    fields = ['question', 'answer']











