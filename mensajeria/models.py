from django.db import models
from django.contrib.auth.models import User

class Messages(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE,related_name="author")
    sendTo=models.ForeignKey(User, on_delete=models.CASCADE,related_name="sendTo")
    message=models.CharField(max_length=500)
    date=models.DateField(auto_now_add=True)

    def __str__(self):
        return (f'{self.author} - {self.sendTo} - {self.date}')
    
