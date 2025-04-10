from django.urls import path
from .views import IndexView, ContactView, BlogView, CourseView, PriceView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('course/', CourseView.as_view(), name='course'),
    path('price/', PriceView.as_view(), name='price'),
]