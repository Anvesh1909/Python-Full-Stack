from django.shortcuts import render,redirect


from app.models import Tasks

from app.forms import TaskForm 

# Create your views here.
def index(request):

    if request.method == "POST":
        data = TaskForm(request.POST)
        if data.is_valid():
            data.save()

    context = {
        'tasks' : Tasks.objects.all(),
        'taskForm' : TaskForm()
    }
    return render(request,'index.html',context)



def update(request,id):
    task = Tasks.objects.get(id=id)

    if request.method == "POST":
        data = TaskForm(request.POST, instance=task)
        if data.is_valid():
            data.save()
        return redirect('index')

    context = {
        'taskForm': TaskForm(instance = task)
    }

    return render(request,'index.html',context)


def delete(request,id):
    task = Tasks.objects.get(id=id)
    task.delete()
    return redirect('index')