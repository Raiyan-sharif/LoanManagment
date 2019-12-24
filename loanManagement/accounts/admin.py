from django.contrib import admin
from accounts.models import UserProfile, Transactions,BankCustomer, LoanModel
# Register your models here.

admin.site.register(UserProfile)

admin.site.register(Transactions)

admin.site.register(BankCustomer)
admin.site.register(LoanModel)