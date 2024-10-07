from django.db import models

class Placement(models.Model):
    student_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    date_placed = models.DateField()

    def __str__(self):
        return self.student_name

class Material(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='materials/')

    def __str__(self):
        return self.title

class Result(models.Model):
    student_name = models.CharField(max_length=100)
    score = models.IntegerField()

    def __str__(self):
        return self.student_name
