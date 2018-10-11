from django.http import HttpResponse

from sth.tasks import some_task


# Create your views here.
def some_view(request):
    result = some_task.delay()

    # Other Methods on Celery AsyncResult
    # result.ready()
    # result.get(timeout=1)
    # result.traceback
    return HttpResponse('some task has being started')
