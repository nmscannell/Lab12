from django.db import models

# Create your models here.


class user(models.Model):
    name = models.CharField(max_length=12, default="")
    password = models.CharField(max_length=12, default="")

    def __str__(self):
        return self.name

class gift(models.Model):
    name = models.CharField(max_length=12, default="")


class usergift(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    gift = models.ForeignKey(gift, on_delete=models.CASCADE)

