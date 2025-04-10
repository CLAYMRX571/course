from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from rest_framework.views import APIView

class IndexView(APIView):
    def get(self, request):
        template = loader.get_template('index.html')
        return HttpResponse(template.render())