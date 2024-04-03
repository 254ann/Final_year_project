# Generated by Django 5.0.2 on 2024-03-15 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0002_transactions_expense_transactions_income'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('food', 'Food'), ('bills', 'Bills'), ('clothing', 'Clothing'), ('shopping', 'Shopping'), ('medical', 'Medical'), ('fun', 'Fun'), ('transport', 'Transport'), ('hospital', 'Hospital'), ('other', 'Other')], max_length=20)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('mode', models.CharField(choices=[('cash', 'Cash'), ('credit_card', 'Credit Card'), ('debit_card', 'Debit Card'), ('cheque', 'Cheque')], max_length=20)),
                ('date_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('salary', 'Salary'), ('business', 'Business'), ('loan', 'Loan'), ('other', 'Other')], max_length=20)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('mode', models.CharField(choices=[('cash', 'Cash'), ('credit_card', 'Credit Card'), ('debit_card', 'Debit Card'), ('cheque', 'Cheque')], max_length=20)),
                ('date_time', models.DateTimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='Transactions',
        ),
    ]