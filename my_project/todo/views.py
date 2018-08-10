from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from . models import todo
from . forms import todoform
import os
# Create your views here.
def todo_list(request):
    print("todo_list-@@@@@@@@@@@@")
    tasks = todo.objects.order_by('id')
    form = todoform()
    context = {'tasks':tasks, 'form':form}
    return render(request, 'todo/todo.html', context)
@require_POST
def addTodo(request):
    print("addTodo-!!!!!!!!!!!!!!")
    form = todoform(request.POST)
    print(form)
    print(request.method)
    print(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
        new_todo = todo(text=request.POST['text'])
        new_todo.save()
    return redirect('list')
def completeTodo(request, pk):
    print("completeTodo-##########")
    toDo = todo.objects.get(pk=pk)
    toDo.complete=True
    toDo.save()
    return redirect('list')
def deleteComplete(request):
    print("deleteComplete-$$$$$$$$$$$")
    todo.objects.filter(complete__exact=True).delete()
    return redirect('list')
def deleteAll(request):
    print("deleteAll-*******")
    todo.objects.all().delete()
    return redirect('list')
