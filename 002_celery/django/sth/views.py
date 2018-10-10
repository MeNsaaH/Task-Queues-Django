from django.http import HttpResponse

from sth.tasks import some_task


# Create your views here.
def some_view(request):
    some_task.delay()
    return HttpResponse('some task has being started')
