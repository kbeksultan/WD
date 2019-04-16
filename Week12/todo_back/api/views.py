import json
from django.http import HttpResponse,JsonResponse
from .models import TaskList
from django.views.decorators.csrf import csrf_exempt
from .serializers import TaskListSerializer,TaskListSerializer2,TaskSerializer

@csrf_exempt
def tasklist_list(request):
    if request.method == 'GET':
        task_lists = TaskList.objects.all()
        # json_tasklists = [t.to_json() for t in task_lists]
        serializer = TaskSerializer(task_lists,many=True)
        return JsonResponse(serializer.data, safe=False,status = 200)
    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = TaskListSerializer2(data=data)
        if serializer.is_valid():
            serializer.save() # create function in serializer class
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors)


@csrf_exempt
def tasklist_detail(request, pk):
    try:
        tasklist = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    return JsonResponse(tasklist.to_json())
    if request.method == 'GET':
        serializer = TaskListSerializer(tasklist)
        return JsonResponse(serializer.data, status=200)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        serializer = TaskListSerializer(instance=category, data=data)
        if serializer.is_valid():
            serializer.save() # update function in serializer class
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors)
    elif request.method == 'DELETE':
        tasklist.delete()
        return JsonResponse({}, status=204)


def tasklist_tasks(request, pk):
    try:
        tasklist = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    tasks = tasklist.task_set.all()
    # json_tasks = [t.to_json() for t in tasks]
    serializer = TaskListSerializer(tasks,many=True)
    return JsonResponse(serializer.data,safe=False)




