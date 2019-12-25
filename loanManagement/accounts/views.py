from django.shortcuts import render, redirect
from accounts.forms import UserForm, LoanForm
from accounts.models import UserProfile
from accounts.models import Transactions
from accounts.models import BankCustomer, LoanModel
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# Create your views here.
from django.contrib.auth import authenticate
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from decimal import Decimal
from django.http import HttpResponse
from django import template
register = template.Library()



from django.contrib import messages
from django.contrib.auth import (authenticate,
                                 login,
                                 logout
                                 )
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404

from .forms import UserRegistrationForm
from .forms import Deposit_form
from .forms import Withdrawl_form
from .forms import BankCustomerForm
from .models import User




def home(request):
    return render(request, 'accounts/home.html')


def user_login(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('user_success'))
        else:
            context["error"] = "Provide valid credentials !!"
            return render(request, "accounts/login.html", context)
    else:
        return render(request, "accounts/login.html", context)

@login_required(login_url="/login/")
def success(request):
    context = {}
    context['user'] = request.user
    return render(request, "accounts/success.html", context)

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('user_login'))





#
# def register_view(request):
#     if request.user.is_authenticated:
#         return redirect("home")
#     else:
#         title = "Create a Bank Account"
#         form = UserRegistrationForm(
#             request.POST or None,
#             request.FILES or None
#             )
#
#         if form.is_valid():
#             user = form.save(commit=False)
#             password = form.cleaned_data.get("password1")
#             user.set_password(password)
#             user.save()
#             new_user = authenticate(email=user.email, password=password)
#             login(request, new_user)
#
#             return redirect("home")
#
#         context = {"title": title, "form": form}
#
#         return render(request, "accounts/form.html", context)

# @register.filter
# def div( value, arg ):
#     '''
#     Divides the value; argument is the divisor.
#     Returns empty string on any error.
#     '''
#     try:
#         value = int( value )
#         arg = int( arg )
#         print(value / arg)
#         if arg: return value / arg
#     except: pass
#     return ''


def register_view(request):  
    if request.user.is_authenticated:
        return redirect("home")
    else:
        title = "Create a Bank Account"
        form = UserRegistrationForm(
            request.POST or None,
            request.FILES or None
            )

        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get("password1")
            user.set_password(password)
            user.save()
            new_user = authenticate(email=user.email, password=password)
            login(request, new_user)

            return redirect("home")

        context = {"title": title, "form": form}

        return render(request, "accounts/form.html", context)

# def deposit(request):
#     if not request.user.is_authenticated:
#         return render(request, "accounts/login.html")
#     else:
#         form = Deposit_form(request.POST or None,
#                             request.FILES or None)
#
#         if form.is_valid():
#             request.user = form.save(commit= False)
#             deposit.user = request.user
#             deposit.user.balance += deposit.user.amount
#             deposit.user.save()
#             deposit.save()
#             return render(request, "accounts/account_details.html")
#
#     context = {
#         "form" : form
#     }
#     return render(request, "accounts/form.html", context)


def deposit(request):
    if not request.user.is_authenticated:
        raise Http404
    else:
        title = "Deposit"
        form = Deposit_form(request.POST or None,
                            request.FILES or None)

        if form.is_valid():
            deposit = form.save(commit=False)
            deposit.user = request.user
            # adds users deposit to balance.
            deposit.user.balance += deposit.amount
            deposit.user.save()
            deposit.save()
            messages.success(request, 'You Have Deposited {} $.'
                             .format(deposit.amount))
            return redirect("home")

        context = {
                    "title": title,
                    "form": form
                  }
        return render(request, "accounts/form.html", context)


def withdrawl(request):
    if not request.user.is_authenticated:
        raise Http404
    else:
        title = "Withdrawl"
        form = Withdrawl_form(request.POST or None)

        if form.is_valid():
            withdrawal = form.save(commit=False)
            withdrawal.user = request.user

            if withdrawal.user.balance >= withdrawal.amount:

                withdrawal.user.balance -= withdrawal.amount
                withdrawal.user.save()
                withdrawal.save()
                return redirect("home")

            else:
                return render(request, "Error You Can't Withdraw Please Return To Previous Page"
                )

        context = {
                    "title": title,
                    "form": form
                  }
        return render(request, "accounts/form.html", context)


@login_required(login_url="/login/")
def account_details(request):
    # if request.user.is_authenticated:
        return render(request, "accounts/account_details.html")




class ListOfBankCustomer(ListView):
    model = BankCustomer
    template_name = 'accounts/customer_list.html'
    # context_object_name = 'my_favorite_publishers'
    def render_to_response(self, context, **response_kwargs):
        """
        Return a response, using the `response_class` for this view, with a
        template rendered with the given context.
        Pass response_kwargs to the constructor of the response class.
        """
        context['title'] = "List of Customer Account"
        context['l'] = BankCustomer.objects.all()
        response_kwargs.setdefault('content_type', self.content_type)
        return self.response_class(
            request=self.request,
            template=self.get_template_names(),
            context=context,
            using=self.template_engine,
            **response_kwargs
        )



class BankCustomerDetail(DetailView):
    model = BankCustomer
    template_name = 'accounts/customer_details.html'


class CustomerLoanDetail(DetailView):
    model = LoanModel
    template_name = 'accounts/customer_loan_details.html'

class CustomerLoanListView(ListView):
    model = LoanModel
    template_name = 'accounts/customer_loan_list.html'






class CustomerLoan(CreateView):
    # success_url = reverse_lazy('/')
    form_class = LoanForm
    template_name = 'accounts/loan_create.html'
    print("ok")

    def get(self, request):
        print(self.content_type)
        print(request.POST)
        form = self.form_class
        context = {'form': form,}
        return render(request, self.template_name, context)

    def post(self, request):
        # print(self.GET)
        print(request.POST)
        form = self.form_class(request.POST)
        if form.is_valid():
            loan = form.save(commit=False)
            # password = user_form.cleaned_data['password1']
            loan_amount = Decimal(request.POST['loan_amount'])
            loan_period = Decimal(request.POST['loan_period'])
            loan_interest_rate = Decimal(request.POST['loan_interest_rate'])
            # playerobj = CustomerLoan.objects.filter(user=self.request.params)
            loan.loan_amount = loan_amount
            loan.loan_period = loan_period
            loan.loan_interest_rate = loan_interest_rate
            net_payable_amount = loan_amount * ((1 + (loan_interest_rate/400))**(4*loan_period/12))
            loan.net_payable_amount = net_payable_amount
            loan.loan_installment_amount = net_payable_amount/loan_period
            loan.save()

        return render(request,self.template_name, {'form': form,})

#
# def transact(request):
#     if not request.user.is_authenticated:
#         return redirect("home")
#     else:
#         transact_variable = [ "deposit", "withdrawl"]
#         if transact_variable == "deposit":
#             list1 = [balance, amount]
#             user = request.user
#             balance = sum(list1)
#             balance.save()
#         else:
#             user= request.user
#             x = subtraction(balance,amount)
#             balance.save()
#
#             context = {
#                 "user": user,
#                 "amount": amount,
#                 "balance": balance,
#                 "transact_variable": transact_variable,
#
#             }
#             return render(request, "accounts/transactions.html", context)

# def register_view(request):  # Creates a New Account & login New users
#     if request.user.is_authenticated:
#         return redirect("home")
#     else:
#         title = "Create a Bank Account"
#         form = UserRegistrationForm(
#             request.POST or None,
#             request.FILES or None
#             )
#
#         if form.is_valid():
#             user = form.save(commit=False)
#             password = form.cleaned_data.get("password1")
#             user.set_password(user.password)
#             user.save()
#             new_user = authenticate(email=user.email, password=password)
#             login(request, new_user)

#
#             return redirect("home")
#
#         context = {"title": title, "form": form}
#
#         return render(request, "accounts/form.html", context)

#
# def subtraction(x,y):
#     total = x - y
#     return total
#
#



# def withdrawl(request):
#     if not request.user.is_authenticated:
#         return Http404
#     else:
#         title = "Withdrawl"
#         form = Withdrawl_form(request.POST or None,
#                             request.FILES or None)
#         if form.is_valid():
#             request.user = form.save(commit= False)
#             withdrawl.user = request.user
#             withdrawl.user.balance -= withdrawl.amount
#             withdrawl.user.save()
#             withdrawl.save()
#             return render(request, "accounts/account_details.html")
#
#     context = {
#         "title" : title,
#         "form" : form
#     }
#     return render(request, "accounts/form.html", context)


# def emp(request):
#     if request.method == "POST":
#         form = UserForm(request.POST)
#         if form.is_valid():
#             try:
#                 form.save()
#                 return redirect('accounts/index.html')
#             except:
#                 pass
#     else:
#         form = UserForm()
#     return render(request,'accounts/index.html',{'form':form})
#
