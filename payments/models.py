from django.db import models
from users.models import User
from django.shortcuts import redirect
class payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    amount= models.IntegerField()
    reason = models.CharField(max_length=300)
    def __str__(self) -> str:
        return 'User'+ str(self.user.username)+ 'Amount: ' + str(self.amount)

class subscription(models.Model):
    cost_of_id_and_volunteer = models.IntegerField()
    def __str__(self):
        return 'cost of id card and volunteer '+ str(self.cost_of_id_and_volunteer) + ' in rupees'
    def save(self, *args, **kwargs):
        if not self.pk and subscription.objects.exists():
            return redirect('admin/payments/subscription/')
        return super(subscription, self).save(*args, **kwargs)