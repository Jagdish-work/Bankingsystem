from django.db import models
from django.urls import reverse

class AccountHolders(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    acct_no = models.IntegerField()
    balance = models.IntegerField()

    def get_absolute_url(self):
        return reverse("account_detail", kwargs={"account_id" : self.id})

    def __str__(self):
        return self.name

class Transactions(models.Model):
    sender = models.ForeignKey(AccountHolders, on_delete=models.CASCADE, related_name='sent')
    receiver = models.ForeignKey(AccountHolders, on_delete=models.CASCADE, related_name='received')
    time = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()

    def __str__(self):
        return str(self.sender) + '->' + str(self.receiver)