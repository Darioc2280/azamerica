from django.urls import path
from .views import PlaygroundPageView, SamplePageView

urlpatterns = [
    path('', PlaygroundPageView.as_view(), name="playground"),
    path('sample', SamplePageView.as_view(), name="Sample"),
]