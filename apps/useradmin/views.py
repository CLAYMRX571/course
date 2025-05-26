from .models import Category, Course, Price, Blog
from django.views.generic import TemplateView, ListView

class CategoryListView(ListView):
    model = Category
    template_name = 'group.html'
    context_object_name = 'categories'

class CourseListView(ListView):
    model = Course
    template_name = 'course.html'
    context_object_name = 'courses'

    def get_queryset(self):
        return Course.objects.filter(category__slug=self.kwargs['slug'])

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
