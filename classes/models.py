from django.db import models
from course.models import Course

class Class(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    class_name = models.CharField(max_length=100)

    def __str__(self):
        return self.class_name
 