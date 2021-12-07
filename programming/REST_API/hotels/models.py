from django import db
from django.core import validators
from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, RegexValidator
from django.core.exceptions import ValidationError
from datetime import date

User = get_user_model()


class Hotel(models.Model):
    booking_number = models.CharField(
        verbose_name="Booking_Number",
        db_index=True,
        unique=True,
        max_length=8,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z]{2}\d{6}$',
                message='Invalid format (should be: 00xxxxxx)',
            )
        ])
    CITIES = (
        (1, "Rome"),
        (2, "Nice"),
        (3, "Berlin"),
    )
    city = models.IntegerField(verbose_name="City", choices=CITIES)
    checkin_datetime = models.DateField(verbose_name='Checkin_Datetime')
    checkout_datetime = models.DateField(verbose_name='Checkout_Datetime')
    guest_name = models.CharField(
        verbose_name='Guest_Name',
        max_length=20,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z]{2,}$',
                message='Only letters are allowed in name',
            )
        ],
    )
    price = models.IntegerField(
        verbose_name='Price',
        validators=[MinValueValidator(limit_value=0, )],
    )
    # user = models.ForeignKey(User,
    #                          verbose_name="User",
    #                          on_delete=models.CASCADE)

    # def save(self, *args, **kwargs):
    #     if self.checkout_datetime < self.checkout_datetime:
    #         raise ValidationError("The date cannot be in the past!")
    #     super(Hotel, self).save(*args, **kwargs)
