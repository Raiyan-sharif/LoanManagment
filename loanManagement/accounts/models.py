from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator
    )
from decimal import Decimal
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import pre_save


GENDER_OPTION = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other')
)

class UserProfile(AbstractUser):
    username = models.CharField('username', max_length=150, unique=True, default="")
    full_name= models.CharField(max_length=50, default="",blank= False)
    password= models.CharField(max_length=50,blank=False, default="")
    birth_date = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True, blank=False)
    contact_no = models.IntegerField(unique=True ,null=True)
    Address = models.CharField(max_length=512)
    city = models.CharField(max_length=256)
    country = models.CharField(max_length=256)
    nationality = models.CharField(max_length=256)
    occupation = models.CharField(max_length=256)
    # account_no = models.PositiveIntegerField(
    #     unique=True,
    #     validators=[
    #         MinValueValidator(10000000),
    #         MaxValueValidator(99999999)
    #         ]
    #     )
    balance = models.DecimalField(
        default=0,
        max_digits=12,
        decimal_places=2
    )


    USERNAME_FIELD = 'email'  # use email to log in
    REQUIRED_FIELDS = ['username']  # required when user is created

    def __str__(self):
        return str(self.username)
    class Meta:
        db_table = "users"

# admin can create bank customer
#bank customer (to whom loan will give loan)
class BankCustomer(models.Model):
    account_no = models.CharField(max_length=150, unique=True, default="")
    full_name = models.CharField(max_length=50, default="", blank=False)
    birth_date = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True, blank=False)
    contact_no = models.CharField(unique=True, null=True, blank=True, max_length=20)
    Address = models.CharField(max_length=512)
    city = models.CharField(max_length=256)
    country = models.CharField(max_length=256)
    nationality = models.CharField(max_length=256)
    occupation = models.CharField(max_length=256)
    monthly_income = models.CharField(max_length=30)

    def __str__(self):
        return self.account_no + " : " + self.full_name


class LoanModel(models.Model):
    customer_id = models.ForeignKey(BankCustomer, on_delete=models.CASCADE, blank=True, null=True,)
    loan_amount = models.DecimalField(null=True, blank=True, default=0.0, max_digits=30, decimal_places=2)
    loan_period = models.IntegerField(null=True, blank=True, default=0)
    loan_status = models.BooleanField(default=False)
    loan_installment_amount = models.DecimalField(null=True, blank=True, default=0.0, max_digits=30, decimal_places=2)
    loan_interest_rate = models.DecimalField(null=True, blank=True, default=0.0, max_digits=30, decimal_places=2)
    net_payable_amount = models.DecimalField(null=True, blank=True, default=0.0, max_digits=30, decimal_places=2)

    def __str__(self):
        return self.pk + " " + self.customer_id + " " + self.loan_amount


# class Accounts(models.Model):
#     user= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
#     balance = models.DecimalField(
#         default=0,
#         max_digits=12,
#         decimal_places=2
#     )
#
#
#     Interest_amount = models.DecimalField(
#       decimal_places=2,
#       max_digits=12,null=True, blank=True
#       )
#     #filter all the transactions in one go
#
#
#     timestamp = models.DateTimeField(auto_now_add=True)
#     def __str__(self):
#         return str(self.account_no)
#


class Transactions(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)


    amount = models.DecimalField(
      decimal_places=2,
      max_digits=12,
        null=True, blank=True
      )

    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.amount)


class CustomerAccount(models.Model):
    account_number = models.CharField('account number', max_length=20, unique=True, default="")
    account_holder_name = models.CharField('username', max_length=150, unique=False, default="")
    birth_day = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_OPTION, default="Male")
    address = models.CharField(max_length=512)
    contact_no = models.IntegerField(unique=True, null=True)
    loan_ammount = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True)
    interest_rate = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True)
    loan_period = models.IntegerField()
    balance = models.IntegerField(null=True,blank=True, default=0)
    # payable_amount
    def getpayable_amout(self):
        return self.loan_ammount * (1+ self.interest_rate/4)**(4*(self.loan_period/12))
