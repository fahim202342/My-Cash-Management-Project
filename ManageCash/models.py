from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUserModel(AbstractUser):
    
    def __str__(self):
        return f'{self.username}'
    

class AddCashModel(models.Model):

#source, datetime, amount, description
    user = models.ForeignKey(
        CustomUserModel,
        on_delete=models.CASCADE,
        related_name='cash_info',
        null=True
        )
    source = models.CharField(max_length=200,null=True)
    datetime = models.DateTimeField(null=True)
    amount = models.FloatField(null=True)
    description = models.TextField(null=True)
    
    def __str__(self):
        return f'{self.user}'
    

class ExpenseModel(models.Model):

    user = models.ForeignKey(
        CustomUserModel,
        on_delete=models.CASCADE,
        related_name='expense_info',
        null=True
    )
    description = models.TextField(null=True)
    amount = models.FloatField(null=True)
    datetime = models.DateTimeField(null=True)

    def __str__(self):
        return f'{self.user}'
    


