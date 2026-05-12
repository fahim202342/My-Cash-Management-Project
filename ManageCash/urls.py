from django.urls import path
from ManageCash.views import *

urlpatterns = [
    path('',register_page, name="register_page"),
    path('login-page/', login_page, name="login_page"),
    path('logout-page/',logout_page, name='logout_page'),
    path('dashboard-page/',dashboard_page, name='dashboard_page'),

    path('cash-list/', cash_list, name="cash_list"),
    path('add-cash/', add_cash, name="add_cash"),
    path('update-cash/<str:id>/', update_cash, name="update_cash"),
    path('delete-cash/<str:id>/', delete_cash, name="delete_cash"),

    path('expense-list/', expense_list, name="expense_list"),
    path('add-expense/', add_expense, name="add_expense"),
    path('update-expense/<str:id>/', update_expense, name="update_expense"),
    path('delete-expense/<str:id>/', delete_expense, name="delete_expense"),

]
