from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    company_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Booking(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True, default=1)
    company_name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    number_of_cookers = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.company_name} booking from {self.start_date} to {self.end_date}"

    # Custom validation for the date range
    def clean(self):
        if not self.start_date or not self.end_date:
            raise ValidationError("Start date and end date must be provided.")
        # Check if the end date is before the start date
        if self.end_date < self.start_date:
            raise ValidationError("End date cannot be earlier than start date.")
        # Optional: Ensure that the booking is not in the past
        if self.start_date < timezone.now().date():
            raise ValidationError("Start date cannot be past current date.")

    # Override save to apply validation automatically
    def save(self, *args, **kwargs):
        self.clean()  # Call the clean method before saving
        super().save(*args, **kwargs)

