from django.db import models
from django.utils import timezone
# Create your models here.

class Blog(models.Model):
    content = models.CharField('本分', max_length=140)
    image = models.ImageField(upload_to='images/', blank=True)
    posted_date = models.DateTimeField('作成日', default=timezone.now)


    def __str__(self):
        return self.content
