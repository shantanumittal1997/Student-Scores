import uuid

from django.db import models

class Student(models.Model):

    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    standard = models.CharField(max_length=20)
    section = models.CharField(max_length=2)
    session = models.IntegerField()

class Subject(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class Score(models.Model):

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='scores')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    score = models.FloatField(default=0.0)

    class Meta:
        unique_together = ('student','subject')