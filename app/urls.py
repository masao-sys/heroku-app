from django.urls import path
from app.views import top

urlpatterns = [
    path('', top.TopView.as_view(), name='top'),
]
