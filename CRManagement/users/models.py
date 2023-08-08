from django.db import models

# Create your models here.
class User(models.Model):
    us_username=models.CharField(max_length=50)
    us_password=models.CharField(max_length=50)
    created_date=models.DateTimeField(auto_now_add=True, blank=True)
    created_by=models.IntegerField(default=0)
    modified_date=models.DateTimeField(auto_now_add=True, blank=True)
    modified_by=models.IntegerField(default=0)

    def __str__(self):
        return self.us_username