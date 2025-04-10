from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from rest_framework.views import APIView

class IndexView(APIView):
    def get(self, request):
        template = loader.get_template('index.html')
        return HttpResponse(template.render())

class ContactView(APIView):
    def get(self, request):
        template = loader.get_template('contact.html')
        return HttpResponse(template.render())

class BlogView(APIView):
    def get(self, request):
        template = loader.get_template('blog.html')
        return HttpResponse(template.render())

class CourseView(APIView):
    def get(self, request):
        template = loader.get_template('course.html')
        return HttpResponse(template.render())

class PriceView(APIView):
    def get(self, request):
        template = loader.get_template('price.html')
        return HttpResponse(template.render())