from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
from .helpers import *
class Blog(models.Model):
    title = models.CharField(max_length=1000)
    content = FroalaField()
    slug = models.SlugField(max_length=1000, null=True, blank=True)
    image = models.ImageField(upload_to='blog')
    created_at = models.DateTimeField(auto_now_add=True)
    upload_to = models.DateTimeField(auto_now=True)
# Create your models here.
def _str_(self):
    return self.titlr
def save(self, *args, **kwargs):
    self.slug = generate_slug(self.title)
    super(Blog, self).save(*args, **kwargs)