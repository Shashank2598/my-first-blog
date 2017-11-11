from django.contrib import admin
from .models import post,Comment,Profile

# Register your models here.

admin.site.register(post)
admin.site.register(Comment)
admin.site.register(Profile)