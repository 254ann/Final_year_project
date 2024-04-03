from django.shortcuts import render, redirect, get_object_or_404
from .models import BillReminder
from .forms import BillReminderForm
from django.contrib.auth.decorators import login_required

@login_required(login_url="login")
def add_bill_reminder(request):
    if request.method == 'POST':
        form = BillReminderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bill_reminder_list')  # Redirect to the bill reminder list page
    else:
        form = BillReminderForm()
    return render(request, 'add_bill_reminder.html', {'form': form})


@login_required(login_url="login")
def bill_reminder_list(request):
    bill_reminders = BillReminder.objects.all()
    return render(request, 'bill_reminder_list.html', {'bill_reminders': bill_reminders})

@login_required(login_url="login")
def delete_bill_reminder(request, reminder_id):
    reminder = get_object_or_404(BillReminder, pk=reminder_id)
    if request.method == 'POST':
        reminder.delete()
        return redirect('bill_reminder_list')  # Redirect to the bill reminder list page
    return render(request, 'delete_bill_reminder.html', {'reminder': reminder})


@login_required(login_url="login")
def bills_home(request):
    return render(request, 'bills_home.html')
