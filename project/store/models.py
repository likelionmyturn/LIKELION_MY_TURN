from django.db import models
from django.contrib.auth.models import User

class Store(models.Model):
    title = models.CharField(max_length=200)
    pup_date = models.DateTimeField('date published')
    body = models.TextField()
    locate = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 
    num = models.IntegerField(default = 0)
    recent_num = models.IntegerField(default=0)
    time = models.IntegerField(default = 0)


    def __str__(self):
        return self.title

class Client(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    # store_num = models.IntegerField(default = 0)
    my_num = models.IntegerField(default = 0)
    phonenum = models.CharField(max_length=10)

    def __str__(self):
        return self.phonenum