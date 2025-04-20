from django.db import models
from clients.models import Client
# Create your models here.
class Loan(models.Model):
    #link to client
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate=models.FloatField()# 5 for 5%
    term_months=models.IntegerField
    start_date=models.DateField()

    STATUS_CHOICES=[
        ('active','Active'),
        ('closed','Closed'),
        ('overdue','Overdue'),
    ]

    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default='active')

    def __str__(self):
        return f"{self.client.full_name} - ${self.amount}"

class repayment(models.Model):
    loan = models.ForeignKey(Loan,on_delete=models.CASCADE)
    date= models.DateField()
    amount=models.DecimalField(max_digits=10, decimal_places=2)
    is_late=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.loan.client.full_name} - Repayment ${self.amount}"