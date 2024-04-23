from typing import Any
from django.db import models


class Staff(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.BigIntegerField()
    join_date = models.DateField()
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.BigIntegerField()
    phone = models.BigIntegerField()

    def __str__(self):
        return self.name

class Payment(models.Model):
    total_amount = models.IntegerField()
    due_amount = models.IntegerField()
    paid_amount = models.IntegerField()
    payment_date = models.DateField()
    due_date = models.DateField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='payments')

class Subject(models.Model):
    subject_name = models.CharField(max_length=100)

    def __str__(self):
        return self.subject_name



class Class(models.Model):
    class_time = models.TimeField(null=True)
    class_count = models.IntegerField()
    teacher = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='classes')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='classes')

    def __str__(self):
        return f'{self.subject} at {self.class_time} by {self.teacher}'


class ClassRegister(models.Model):
    classes = models.ForeignKey(Class,on_delete=models.CASCADE,related_name='registration')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='registration')
    marks = models.IntegerField(default=0)

class SuperKey(models.Model):
    payment_id = models.ForeignKey(Payment,on_delete=models.CASCADE)
    class_reg_id = models.ForeignKey(ClassRegister,on_delete=models.CASCADE)