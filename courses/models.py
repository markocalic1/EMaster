from django.db import models
from django.core.urlresolvers import reverse

class Course(models.Model):
    name = models.CharField(max_length=25)
    logo = models.FileField(null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    def get_absolute_url(self):
        return reverse('courses:detail', kwargs={'pk':self.pk})

    def _str_(self):
        # string repreetnacija objekta
        return self.name


class Chapter(models.Model):
    name = models.CharField(max_length=25)
    date_created = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def _str_(self):
        # string repreetnacija objekta
        return   self.chapter_name

class Block(models.Model):
    title = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    chapter = models.ForeignKey(Chapter)

class TextBlock(Block):
    text = models.TextField()

class VideoBlock(Block):
    link = models.FileField(null=False, blank=False)

class ImageBlock(Block):
    image = models.FileField()

class QuizBlock(Block):
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)

