from django.http import JsonResponse
from rest_framework import viewsets
from .models import Project, Task
from .serializers import ProjectSerializer, TaskSerializer


from rest_framework.decorators import api_view


def health_check(request):
    return JsonResponse({"status": "ok", "service": "1era clase Python (Que Lio) API"})


@api_view(["GET"])
def trigger_500(request):
    """Endpoint de prueba para verificar respuesta 500 del custom_exception_handler"""
    raise RuntimeError("Error interno no controlado para prueba")


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.select_related("project").prefetch_related("tags").all()
    serializer_class = TaskSerializer