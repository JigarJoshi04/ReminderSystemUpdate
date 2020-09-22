from django.db import models

# Create your models here.
class ScheduleTaskModel(models.Model):
    service_name = models.CharField(max_length=100)
    service_type = models.CharField(max_length=100)
    date_of_deadline = models.DateField()
    actual_date_on_which_reminder_is_to_be_sent = models.DateField()
    recurrence_type = models.IntegerField()
    email_data = models.CharField(max_length=500)

class CompletedMailModel(models.Model):
    email = models.CharField(max_length=100)
    pan = models.CharField(max_length=100)
    client_name = models.CharField(max_length=100)
    service_type = models.CharField(max_length=100)
    date_of_deadline = models.DateField()
    actual_date_on_which_reminder_is_to_be_sent = models.DateField()
    