from django.shortcuts import render, redirect
from ManageCash.forms import *
from django.contrib import messages
from django.contrib.auth import login, logout
from django.db.models import Sum
from django.contrib.auth.decorators import login_required

def register_page(request):
    if request.method == "POST":
        form_data = RegistrationForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            messages.success(request, 'Registration Successfully')
            return redirect('login_page')

    form_data = RegistrationForm()
    context = {
        'form_data':form_data,
        'form_title':'User Registration Form',
        'form_btn': 'Register'
    }
    return render(request, 'master/base-form.html',context)

def login_page(request):
    if request.method == 'POST':
        form_data = LoginForm(request, request.POST)
        if form_data.is_valid():
            user = form_data.get_user()
            login(request, user)
            messages.success(request, 'Login Successfully')
            return redirect('dashboard_page')

    form_data = LoginForm()
    context = {
        'form_data':form_data,
        'form_title':'Login Form',
        'form_btn': 'Login'
    }   
    return render(request, 'master/base-form.html',context) 

@login_required
def logout_page(request):
    
    logout(request)
    return redirect('login_page')

@login_required
def dashboard_page(request):

    cash_data = AddCashModel.objects.filter(user=request.user)
    expense_data = ExpenseModel.objects.filter(user=request.user)

    total_cash = cash_data.aggregate(
        total=Sum('amount')
    )['total'] or 0

    total_expense = expense_data.aggregate(
        total=Sum('amount')
    )['total'] or 0

    current_balance = total_cash - total_expense

    context = {
        'cash_data': cash_data,          
        'expense_data': expense_data,    
        'total_cash': total_cash,
        'total_expense': total_expense,
        'current_balance': current_balance,
    }

    return render(request, 'dashboard.html', context)


@login_required
def cash_list(request):

    cash_data = AddCashModel.objects.filter(user=request.user)
    context = {
        'cash_data': cash_data

    }
    return render(request, 'cash-list.html',context)


@login_required
def add_cash(request):
    if request.method == 'POST':
        form_data = AddCashForm(request.POST)
        if form_data.is_valid():
            data = form_data.save(commit=False)
            data.user = request.user
            data.save()
            messages.success(request, 'Add Cash Successfully')
            return redirect('cash_list')
      
    form_data = AddCashForm()
    context = {
        'form_data':form_data,
        'form_title':'Add Cash Page',
        'form_btn': 'Add Cash'
    }  
    return render(request, 'master/base-form.html',context)


@login_required
def update_cash(request, id):
    cash_data = AddCashModel.objects.get(id=id)
    if request.method == 'POST':
        form_data = AddCashForm(request.POST,instance=cash_data)
        if form_data.is_valid():
            data = form_data.save(commit=False)
            data.user = request.user
            data.save()
            messages.success(request, 'Add Cash Successfully')
            return redirect('cash_list')
      
    form_data = AddCashForm(instance=cash_data)
    context = {
        'form_data':form_data,
        'form_title':'Update Cash Page',
        'form_btn': 'Update Cash'
    }  
    return render(request, 'master/base-form.html',context)


@login_required
def delete_cash(request, id):

    AddCashModel.objects.get(id=id).delete()
    messages.success(request, 'Cash Delete Successfully')
    return redirect('cash_list')


@login_required
def expense_list(request):
    expense_data = ExpenseModel.objects.filter(user=request.user)
    context = {
        'expense_data': expense_data
    }
    return render(request, 'expense-list.html',context)


@login_required
def add_expense(request):
    if request.method == 'POST':
        form_data = ExpenseForm(request.POST)
        if form_data.is_valid():
            data = form_data.save(commit=False)
            data.user = request.user
            data.save()
            messages.success(request, 'Add Expense Successfully')
            return redirect('expense_list')
    
    form_data = ExpenseForm()
    context = {
        'form_data': form_data,
        'form_title': 'Add Expense Page',
        'form_btn': 'Add Expense',
    }
    return render(request, 'master/base-form.html', context)


@login_required
def update_expense(request, id):
    cash_data = ExpenseModel.objects.get(id=id)
    if request.method == 'POST':
        form_data = ExpenseForm(request.POST,instance=cash_data)
        if form_data.is_valid():
            data = form_data.save(commit=False)
            data.user = request.user
            data.save()
            messages.success(request, 'Update Expense Successfully')
            return redirect('expense_list')
      
    form_data = ExpenseForm(instance=cash_data)
    context = {
        'form_data':form_data,
        'form_title':'Update Expense Page',
        'form_btn': 'Update Expense'
    }  
    return render(request, 'master/base-form.html',context)


@login_required
def delete_expense(request, id):

    ExpenseModel.objects.get(id=id).delete()
    messages.success(request, 'Expense Delete Successfully')
    return redirect('expense_list')



