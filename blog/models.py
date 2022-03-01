from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Category(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    
class Post(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='Published')

    class Meta:
        ordering=('-published',)
    

    STATUS = (
        ('Draft', 'Draft'),
        ('Published', 'Published')

    )
    category = models.ForeignKey(Category, verbose_name=('category'), on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=250)
    excert = models.CharField(max_length=250, null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, verbose_name='Author', on_delete=models.CASCADE, related_name='blog_posts')
    status = models.CharField(max_length=20, choices=STATUS, default='published')
    objects = models.Manager()
    postobjects = PostObjects()

    def __str__(self):
        return self.title

