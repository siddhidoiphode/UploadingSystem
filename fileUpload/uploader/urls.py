from django.urls import path
from .views import upload_content

urlpatterns = [
    path('', upload_content, name='upload_content'),
]
