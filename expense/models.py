# In models.py

from django.db import models

class Income(models.Model):
    CATEGORY_CHOICES = (
        ('salary', 'Salary'),
        ('business', 'Business'),
        ('loan', 'Loan'),
        ('other', 'Other'),
    )
    MODE_CHOICES = (
        ('cash', 'Cash'),
        ('mpesa', 'Mpesa'),
        ('credit_card', 'Credit Card'),
        ('debit_card', 'Debit Card'),
        ('cheque', 'Cheque'),
    )
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    mode = models.CharField(max_length=20, choices=MODE_CHOICES)
    date_time = models.DateTimeField()

    def __str__(self):
        return f"Income - {self.category} - {self.amount} - {self.mode}"


class Expense(models.Model):
    CATEGORY_CHOICES = (
        ('food', 'Food'),
        ('bills', 'Bills'),
        ('clothing', 'Clothing'),
        ('shopping', 'Shopping'),
        ('medical', 'Medical'),
        ('fun', 'Fun'),
        ('transport', 'Transport'),
        ('hospital', 'Hospital'),
        ('other', 'Other'),
    )
    MODE_CHOICES = (
        ('cash', 'Cash'),
         ('mpesa', 'Mpesa'),
        ('credit_card', 'Credit Card'),
        ('debit_card', 'Debit Card'),
        ('cheque', 'Cheque'),
    )
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    mode = models.CharField(max_length=20, choices=MODE_CHOICES)
    date_time = models.DateTimeField()

    def __str__(self):
        return f"Expense - {self.category} - {self.amount} - {self.mode}"
