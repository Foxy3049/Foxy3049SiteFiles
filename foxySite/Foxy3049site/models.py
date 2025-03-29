from django.db import models

class Register(models.Model):
    email = models.CharField(max_length=200)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    send_data = models.DateTimeField('Data send')
    def __str__(self):
        return f"{self.email} {self.username} {self.password}"
