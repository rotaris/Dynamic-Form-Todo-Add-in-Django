from django.db import models

class TodoList(models.Model):
    name = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.name

class TodoItem(models.Model):
    name = models.CharField(max_length=150, help_text="e.g. Buy milk, wash dog etc")
    list = models.ForeignKey(TodoList)
    
    def __unicode__(self):
        return self.name + " (" + str(self.list) + ")"

