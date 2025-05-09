from django.urls import path
from .views import CategoryListView, CourseListView, PriceListView, BlogView, ContactView

urlpatterns = [
    path('category/', CategoryListView.as_view(), name='categories'),
    path('courses/', CourseListView.as_view(), name='courses'),
    path('price/', PriceListView.as_view(), name='prices'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('contact/', ContactView.as_view(), name='contact'),
]