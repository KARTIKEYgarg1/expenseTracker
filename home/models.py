from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
TYPE = (
    ('Postive','Positive'),
    ('Negative','Negative')
)
class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    income=models.FloatField()
    expense=models.FloatField(blank=True,default=0)
    balance=models.FloatField(blank=True)

# Create your models here.
class Expense(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    amount=models.FloatField(blank=True,default=0)
    name=models.CharField(max_length=100)
    expense_type=models.CharField(max_length=100,choices=TYPE)
    def __str__(self):
        return self.name