from django.contrib import admin

from .models import AccountHolders, Transactions

admin.site.register(AccountHolders)
admin.site.register(Transactions)
