from django import forms
from django.db import models
from accounts.models import UserProfile
from accounts.models import Transactions
from accounts.models import BankCustomer, LoanModel
import datetime
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
# from django.forms.extras.widgets import SelectDateWidget
class BankCustomerForm(forms.ModelForm):
    class Meta:
        models = BankCustomer
        fields = "__all__"

class UserForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = "__all__"




from .models import User


class UserRegistrationForm(UserCreationForm):
    birth_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        model = UserProfile
        fields = [
                  "username",
                  "full_name",
                  "birth_date",
                  "email",
                  "contact_no",
                  "Address",
                  "city",
                  "country",
                  "nationality",
                  "occupation",
                  "password1",
                  "password2"
                  ]

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['full_name']
        user.birth_date = self.cleaned_data['birth_date']
        if commit:
            user.save()
        return user


class Deposit_form(forms.ModelForm):
    class Meta:
        model = Transactions
        fields = [
            'amount'
        ]

class Withdrawl_form(forms.ModelForm):
    class Meta:
        model = Transactions
        fields = [
            'amount'
        ]

class LoanForm(forms.ModelForm):
    class Meta:
        model = LoanModel
        fields = ['customer_id','loan_amount', 'loan_period', 'loan_interest_rate']

class DisbursementForm(forms.ModelForm):
    class Meta:
        model = LoanModel
        fields = ['id','disbursement_status','account_balance','net_payable_amount']
        # email = forms.CharField(disabled=True)

class InstallmentAmount(forms.ModelForm):
    class Meta:
        model = LoanModel
        fields = ['id','loan_installment_amount','account_balance']