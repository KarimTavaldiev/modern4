# from django.contrib.auth.models import AbstractUser
# from django.db import models
#
#
#
#
# class Category(models.Model):
#     slug = models.SlugField(primary_key=True, max_length=50)
#     name = models.CharField(max_length=50)
#     image = models.ImageField(upload_to='categories', blank=True, null=True)
#
# #
# class Mark(models.Model):
#     title = models.CharField(max_length=50)
#     description = models.PositiveIntegerField()
#     created = models.DateTimeField()
#
#     def __str__(self):
#         return self.title
