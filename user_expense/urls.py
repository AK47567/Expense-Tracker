from django.urls import path
from .views import UserData_viewset, SavingsViewSet, ExpensesViewSet, CategoryViewSet

urlpatterns = [
    path('userdata/', UserData_viewset.as_view({'get': 'list', 'post': 'create'}), name='userdata-list'),
    path('userdata/<int:pk>/', UserData_viewset.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='userdata-detail'),
    path('savings/', SavingsViewSet.as_view({'get': 'list', 'post': 'create'}), name='savings-list'),
    path('savings/<int:pk>/', SavingsViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='savings-detail'),
    path('expenses/', ExpensesViewSet.as_view({'get': 'list', 'post': 'create'}), name='expenses-list'),
    path('expenses/<int:pk>/', ExpensesViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='expenses-detail'),
    path('category/', CategoryViewSet.as_view({'get': 'list', 'post': 'create'}), name='category-list'),
    path('category/<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='category-detail'),
]
