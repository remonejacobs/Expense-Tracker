from django.db import models

# Create your models here.
class Expense(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    category = models.CharField(max_length=100)
    expense_name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.expense_name
