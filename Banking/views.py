from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q

from .models import AccountHolders, Transactions
from .forms import MoneyTransferForm

def index(request):
    accounts = AccountHolders.objects.all()
    return render(
        request,
        'banking/index.html',
        {'accounts': accounts}
    )

def transaction_history(request):
    transactions = Transactions.objects.order_by('-time')
    return render(
        request,
        'banking/transaction_history.html',
        {'transactions' : transactions}
    )

def transfer_money(request):
    accounts = AccountHolders.objects.all()
    if request.method == 'POST':
        form = MoneyTransferForm(request.POST, initial={'accounts': accounts})
        if form.is_valid():
            transfer = form.save()
            amount = transfer.amount
            sender = transfer.sender
            receiver = transfer.receiver
            # Actual transfer of money
            sender.balance -= amount
            receiver.balance += amount
            sender.save()
            receiver.save()
            messages.success(request, "Money: `{0}` Transferred from `{1}` to `{2}`".format(amount, sender, receiver))
            return redirect('index')
        else:
            # Form is not valid, send back with errors
            return render(
                request,
                'banking/money_transfer.html',
                {'form': form}
            )
    else:
        form = MoneyTransferForm(initial={'accounts': accounts})
        return render(
            request,
            'banking/money_transfer.html',
            {'form': form}
        )

def account_detail(request, account_id):
    account = get_object_or_404(AccountHolders, id=account_id)
    transactions = Transactions.objects.filter(Q(sender=account) | Q(receiver=account))
    return render(
        request,
        'banking/account_detail.html',
        {'account': account, 'transactions': transactions}
    )