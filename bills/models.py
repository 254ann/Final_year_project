from django.db import models

# Create your models here.
class BillReminder(models.Model):
    CATEGORY_CHOICES = (
        ('electricity', 'Electricity'),
        ('internet', 'Internet'),
        ('rent', 'Rent'),
        ('insurance', 'Insurance'),
        ('water', 'Water'),
        ('other', 'Other'),
    )
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()

    def __str__(self):
        return f"Bill Reminder - {self.title} - {self.amount} - Due {self.due_date}"
