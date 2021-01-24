from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import Posts

urlpatterns = [
    path('posts/', csrf_exempt(Posts.as_view())),
]