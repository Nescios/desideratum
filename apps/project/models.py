from django.db import models


# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    
    def registered_time(self):
        return sum(entry.minutes for entry in self.entries.all())


class Task(models.Model):
    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']
    
    def __str__(self) -> str:
        return self.title

    def registered_time(self):
        return sum(entry.minutes for entry in self.entries.all())


class Entry(models.Model):
    project = models.ForeignKey(Project, related_name='entries', on_delete=models.CASCADE, blank=True, null=True)
    task = models.ForeignKey(Task, related_name='entries', on_delete=models.CASCADE, blank=True, null=True)
    minutes = models.PositiveIntegerField(default=0)
    is_tracked = models.BooleanField(default=False)
    created_at = models.DateTimeField()

    class Meta:
        ordering = ['created_at']

        def __str__(self):
            if self.task:
                return '%s - %s' % (self.task.title, self.created_at)
            
            return '%s' % self.created_at