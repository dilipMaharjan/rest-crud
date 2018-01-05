from django.db import models


class Todo(models.Model):
    STATUSES = (
        (0, 'Done',),
        (1, 'UnDone')
    )
    title = models.CharField(max_length=50)
    status = models.IntegerField(choices=STATUSES, default=1)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title
