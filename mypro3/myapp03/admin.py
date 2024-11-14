from django.contrib import admin
from .models import Loan, LoanAdmin
admin.site.register(Loan, LoanAdmin)

# Register your models here.
