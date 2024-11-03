# Create your models here.

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    # Additional fields can be added here
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups',  # Change this to a unique name
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',  # Change this to a unique name
        blank=True,
    )

class IPODetails(models.Model):

    #Listing Information (upcoming)
    STATUS_CHOICES = [
        (0, 'Coming Soon'),
        (1, 'Ongoing'),
        (2, 'Listed'),
    ]

    ISSUE_TYPE_CHOICES = [
        ('BB', 'Book Built'),
        ('RB', 'Red Herring'),
        ('OP', 'Open Price'),
    ]

    id = models.BigAutoField(primary_key=True)
    company_logo_path = models.TextField()
    company_name = models.CharField(max_length=255)
    price_band = models.CharField(max_length=50)
    open_date = models.CharField(max_length=50)
    close_date = models.CharField(max_length=50)
    issue_size = models.CharField(max_length=50)
    issue_type = models.CharField(max_length=2, choices=ISSUE_TYPE_CHOICES)
    listing_date = models.CharField(max_length=50)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)

    #After Listed then update details
    ipo_price = models.CharField(max_length=50)
    listing_price = models.CharField(max_length=50)
    listing_gain = models.CharField(max_length=50)
    cmp = models.CharField(max_length=50)
    current_return = models.CharField(max_length=50)

    #if avilable enter 
    rhp = models.CharField(max_length=255)
    drhp = models.CharField(max_length=255)

    #user foreigkey
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ipo_details')

    def __str__(self):
        return self.company_name
