from django.db import models

class register(models.Model):
    name=models.TextField()
    email=models.EmailField()
    age=models.IntegerField()
    password=models.TextField()
    
class Files(models.Model):
    user = models.ForeignKey(register, on_delete=models.CASCADE)
    title = models.TextField()
    file = models.FileField(upload_to='uploads/' , null=True, blank=True)