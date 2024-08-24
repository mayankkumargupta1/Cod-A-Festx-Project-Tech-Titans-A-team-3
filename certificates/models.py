from django.db import models
import uuid
from django.core.validators import RegexValidator
from users.models import User

phone_regex = RegexValidator(
    regex=r'^\d{10}$',
    message="Phone number must be entered in the format: '9999999999'. Exactly 10 digits allowed."
)


class certificate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Full_name = models.CharField(max_length=300)
    Description = models.TextField()
    Date = models.DateField(auto_now_add=True)
    Phone_number = models.CharField(validators=[phone_regex], max_length=10, blank=True)

    def __str__(self):
        return "USER: {} ID: {} NAME: {} DATE: {}".format(self.user.username,self.id, self.Full_name, self.Date)