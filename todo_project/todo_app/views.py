from rest_framework import generics, permissions, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Todos
from .serializers import TodoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        status_param = self.request.query_params.get('status')
        tasks = Todos.objects.filter(user=self.request.user)
        if status_param:
            tasks = tasks.filter(status=status_param)
        return tasks

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Todos.objects.filter(user=self.request.user)

class MarkAsCompleted(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            task = Todos.objects.get(pk=pk, user=request.user)
            task.status = 'Completed'
            task.save()
            return Response({'status': 'Task marked as completed'}, status=status.HTTP_200_OK)
        except Todos.DoesNotExist:
            return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Todos.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Todos.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CustomPagination(PageNumberPagination):
    page_size = 5

class TaskListView(generics.ListAPIView):
    queryset = Todos.objects.all()
    serializer_class = TodoSerializer
    pagination_class = CustomPagination


# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from .models import Todos
# from .serializers import TodoSerializer

# @api_view(['GET'])
# def todo_list(request):
#     todos = Todos.objects.all()
#     serializer = TodoSerializer(todos, many=True)
#     return Response(serializer.data)

# @api_view(['POST'])
# def create_todo(request):
#     serializer = TodoSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors)


# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from .models import Todos
# from .forms import ListForm


# def index(request):
#     if request.method == "POST":
#         form = ListForm(request.POST or None)
#         if form.is_valid:
#             form.save()
#             todo_list = Todos.objects.all()
#             return render(request,"todo_app/index.html", {'todo_list':todo_list})

#     else:
#         todo_list = Todos.objects.all()
#         return render(request,"todo_app/index.html", {'todo_list':todo_list})

# def about(request):
#     return render(request,"todo_app/about.html")

# def create(request):
#     if request.method == "POST":
#         form = ListForm(request.POST or None)
#         if form.is_valid:
#             form.save()
#             todo_list = Todos.objects.all()
#             return render(request,"todo_app/create.html", {'todo_list':todo_list})

#     else:
#         todo_list = Todos.objects.all()
#         return render(request,"todo_app/create.html", {'todo_list':todo_list})

# def delete(request, Todos_id):
#     todo = Todos.objects.get(pk=Todos_id)
#     todo.delete()
#     return redirect("index")

# def yes_finish(request, Todos_id):
#     todo = Todos.objects.get(pk=Todos_id)
#     todo.finished = False
#     todo.save()
#     return redirect("index")

# def no_finish(request, Todos_id):
#     todo = Todos.objects.get(pk=Todos_id)
#     todo.finished = True
#     todo.save()
#     return redirect("index")

# def update(request, Todos_id):
#     if request.method == "POST":
#         todo_list = Todos.objects.get(pk=Todos_id)
#         form = ListForm(request.POST or None, instance=todo_list)
#         if form.is_valid:
#             form.save()
#             return redirect("index")

#     else:
#         todo_list = Todos.objects.all()
#         return render(request,"todo_app/update.html", {'todo_list':todo_list})