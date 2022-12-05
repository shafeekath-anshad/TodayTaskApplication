from django.shortcuts import render, redirect
from .models import today_task
from .forms import todayform
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView


class TaskListView(ListView):
    model = today_task
    template_name = "index.html"
    context_object_name = 'task_results'


class TaskDetailView(DetailView):
    model = today_task
    template_name = "details.html"
    context_object_name = 'i'


class TaskUpdateView(UpdateView):
    model = today_task
    template_name = "update.html"
    context_object_name = 'formresult'
    fields = ('Take_name', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('cbvdetails', kwargs={'pk': self.object.id})


class TaskDeleteView(DeleteView):
    model = today_task
    template_name = "delete.html"

    def get_success_url(self):
        return reverse_lazy('cbvindex', kwargs={'pk': self.object.id})


# Create your views here.
def index(request):
    task = today_task.objects.all()
    if request.method == 'POST':
        Take_name = request.POST.get('taskname')
        priority = request.POST.get('priority')
        date = request.POST.get('date')
        task = today_task(Take_name=Take_name, priority=priority, date=date)
        task.save()
        return redirect('/')
    return render(request, "index.html", {'task_results': task})


def delete(request, taskid):
    task = today_task.objects.get(id=taskid)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, "delete.html")


def update(request, id):
    taskvar = today_task.objects.get(id=id)
    form = todayform(request.POST or None, instance=taskvar)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, "update.html", {'formresult': form, 'taskresult': taskvar})
