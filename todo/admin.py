from dynamicform.todo.models import *
from django.contrib import admin

admin.site.register(TodoItem)

class TodoItemAdmin(admin.TabularInline):
    model = TodoItem
    extra = 0

class TodoListAdmin(admin.ModelAdmin):
    inlines = [TodoItemAdmin]

admin.site.register(TodoList, TodoListAdmin)
