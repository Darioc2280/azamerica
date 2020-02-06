from django.urls import path
from .views import PageListView, PageDetailView, PageCreate, PageUpdate, PageDelete

pages_patterns = ([
    path('', PageListView.as_view(), name='pagesplay'),
    path('<int:pk>/<slug:slug>/', PageDetailView.as_view(), name='pageplay'),
    path('create/', PageCreate.as_view(), name='create'),
    path('update/<int:pk>', PageUpdate.as_view(), name='update'),
    path('delete/<int:pk>', PageDelete.as_view(), name='delete'),

    ], 'pagesplay')