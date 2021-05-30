from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
# Create your models here.
class Document(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    content = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.name+'.docx'
    
    def get_absolute_url(self):
        return reverse('create')

