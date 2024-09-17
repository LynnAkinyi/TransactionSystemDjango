from django.db import models

# Create your models here.

class Transaction(models.Model):
    account_id = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.account_id} - {self.amount}"
