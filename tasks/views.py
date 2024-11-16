from rest_framework import viewsets
from .models import Task, Category, Comment
from .serializers import TaskSerializer, CategorySerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import ModelViewSet


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['priority', 'completed', 'category__name']
    ordering_fields = ['priority', 'due_date', 'title']
    ordering = ['due_date']

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer