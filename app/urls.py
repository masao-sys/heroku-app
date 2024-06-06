from django.urls import path, include
from app.views import top, credit, item

urlpatterns = [
    path('', top.TopView.as_view(), name='top'),
    path('accounts/', include('allauth.urls')),

    path('credit/register/', credit.CreditRegisterView.as_view(), name='credit-register'),
    path('credit/update/', credit.CreditUpdateView.as_view(), name='credit-update'),
    path('subscription/cancel/', credit.SubscriptionCancelView.as_view(), name='subscription-cancel'),

    path('item/', item.ItemListView.as_view(), name='item-list'),
    path('item/create/', item.ItemCreateView.as_view(), name='item-create'),
    path('item/update/<int:pk>/', item.ItemUpdateView.as_view(), name='item-update'),
    path('item/delete/<int:pk>/', item.ItemDeleteView.as_view(), name='item-delete'),
]
