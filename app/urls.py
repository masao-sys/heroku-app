from django.urls import path, include
from app.views import top

urlpatterns = [
    path('', top.TopView.as_view(), name='top'),
    path('accounts/', include('allauth.urls')),
]
