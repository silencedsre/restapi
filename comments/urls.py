from django.urls import path, include
from .views import comment_view, form_view
app_name = 'comments'
urlpatterns = [
    path('', comment_view, name='comment'),
    path('form/', form_view, name='form'),
]