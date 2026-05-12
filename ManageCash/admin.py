from django.contrib import admin
from ManageCash.models import *


admin.site.register([CustomUserModel,AddCashModel,ExpenseModel])
