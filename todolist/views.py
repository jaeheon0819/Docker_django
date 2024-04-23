from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm # type: ignore

def todo_list(request):
    todos = Todo.objects.filter(completed = False)
    completed_todos = Todo.objects.filter(completed=True)
    return render(request, 'todolist/todo_list.html', {'todos': todos, 'completed_todos':completed_todos})

def complete_todo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.completed = True
    todo.save()
    return redirect('todo_list')

def delete_completed(request):
    Todo.objects.filter(complted=True).delete()
    return redirect('todo_list')

def delete_all(request):
    Todo.objects.all().delete()
    return redirect('todo_lsit')

def edit_todo(request, todo_id):
    todo=get_object_or_404(Todo, id=todo_id)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todolist/edit_todo.html', {'form': form})

def add_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'todo/add_todo.html', {'form': form})
