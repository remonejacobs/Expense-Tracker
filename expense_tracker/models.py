from django.db import models

# Create your models here.
class Expense(models.Model):
    CATEGORY_CHOICES = [
        ("Fixed/Essential", "Fixed/Essential"),
        ("Food & Daily Living", "Food & Daily Living"),
        ("Transportation", "Transportation"),
        ("Personal & Lifestyle", "Personal & Lifestyle"),
        ("Health & Wellness", "Health & Wellness"),
        ("Education", "Education"),
        ("Entertainment & Social", "Entertainment & Social"),
        ("Work/Business", "Work/Business"),
        ("Giving & Miscellaneous", "Giving & Miscellaneous"),
    ]

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    expense_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.expense_name
