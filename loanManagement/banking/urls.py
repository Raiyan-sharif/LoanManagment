"""banking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from accounts.views import (user_login, user_logout,
    success, home, account_details, register_view, deposit,withdrawl, ListOfBankCustomer, BankCustomerDetail,
                            CustomerLoan, CustomerLoanListView,CustomerLoanDetail)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('account/', include('accounts.urls')),
    path('login/', user_login, name="user_login"),
    path('success/', success, name="user_success"),
    path('logout/', user_logout, name="user_logout"),
    path('account_details/', account_details, name="account_details"),
    path('register_view/', register_view, name= "register_view"),
    path('deposit/', deposit, name= "deposit"),
    path('withdrawl/',withdrawl, name= 'withdrawl'),
    path('customer_list/',ListOfBankCustomer.as_view(),name='customer_list'),
    path('customer_details/<int:pk>/', BankCustomerDetail.as_view(), name='customer_details'),
    path('create_loan/', CustomerLoan.as_view(), name='loan_create'),
    path('customer_loan_list/',CustomerLoanListView.as_view(), name='customer_loan_list'),
    path('customer_loan_details/<int:pk>/',CustomerLoanDetail.as_view(), name='customer_loan_details'),
    # path('transact/', transact, name="transact"),
]
