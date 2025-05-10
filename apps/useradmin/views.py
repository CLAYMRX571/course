from django.views.generic import TemplateView
from .models import Category, Course, Price, Blog
from django.views.generic import ListView
from django.shortcuts import render

class CategoryListView(ListView):
    model = Category
    template_name = 'group.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return Category.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = self.get_queryset()
        return context

class CourseListView(ListView):
    model = Course
    template_name = 'course.html'
    context_object_name = 'courses'

    def get_queryset(self):
        return Course.objects.all()

class PriceListView(ListView):
    model = Price
    template_name = 'price.html'
    context_object_name = 'prices'

    def get_queryset(self):
        return Price.objects.all()

class BlogView(ListView):
    model = Blog
    template_name = 'blog.html'
    context_object_name = 'prices'

    def get_queryset(self):
        return Price.objects.all()

class ContactView(TemplateView):
    template_name = "contact.html"
