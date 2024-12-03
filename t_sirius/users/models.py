from django.db import models

# Create your models here.
class test_Details(models.Model):
    STATUS_CHOICES = [
        ('Online','Online'),
        ('Offline','Offline'),
        ('Suspend','Suspend'),
    ]

    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    email_address = models.EmailField(max_length=100, unique=True)
    user_address = models.CharField(max_length=200)
    user_password = models.CharField(max_length=100, null=False)
    date_joined = models.DateTimeField(auto_now_add=True)

class test_Vehicle_Profile(models.Model):
    user = models.OneToOneField(
        test_Details,
        on_delete=models.CASCADE,
        related_name = "vehicle_profile"
    )
    mirror_angle = models.FloatField()
    seat_height = models.FloatField()
    seat_angle = models.FloatField()
    ambient_color = models.CharField(max_length=30)
