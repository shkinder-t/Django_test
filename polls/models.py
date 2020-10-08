
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from django.shortcuts import reverse
from django.utils import timezone
from datetime import timedelta


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', auto_now_add= True)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.question_text

    def save(self, *args, **kwargs):
        self.slug = slugify(self.question_text)[:10]
        super(Question, self).save(*args, **kwargs)

    def was_published_recently(self):
        curent_time = timezone.now()
        day_ago = curent_time - timedelta(days=1)
        return day_ago < self.pub_date <curent_time

    def get_absolute_url(self):
        return reverse('polls:detail', args=[str(self.slug)])


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def get_absolute_url(self):
      return reverse('polls:detail', args=(self.question.id,))


class UsersChoise(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)


class Meta:
    unique_together = ('user_id', 'choice_id')






