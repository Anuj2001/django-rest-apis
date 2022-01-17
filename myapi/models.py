from django.db import models

class Profile(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    phone_no=models.BigIntegerField()
    address=models.TextField()

    def __str__(self):
        return str(self.email)

