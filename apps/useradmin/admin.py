from django.contrib import admin
from .models import Category, Course, Price, Blog

admin.site.register(Course)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Price)
admin.site.register(Blog)