from django.contrib import admin
from .models import Category, Course, Price

admin.site.register(Course)
admin.site.register(Category)
admin.site.register(Price)