from django.db import models


# Create your models here.
class BookModel(models.Model):
    objects = None
    image = models.ImageField(upload_to='images/', null=True)
    author = models.CharField(max_length=125)
    name = models.CharField(max_length=255)
    description = models.TextField()
    pages = models.IntegerField()
    ebooks = models.FileField(upload_to='ebooks/')

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name


