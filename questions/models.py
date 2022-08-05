from django.db import models

# Create your models here.
class users(models.Model):
    sname = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    upass = models.CharField(max_length=100)
    
    def __str__(self):
        return self.user

class post_q(models.Model):
    pquestion = models.CharField(max_length=1000)
    puser = models.CharField(max_length=100)
    
    def __str__(self):
        return self.pquestion

class qna_db(models.Model):
    qid = models.CharField(max_length=100)
    answr = models.CharField(max_length=1000)
    auser = models.CharField(max_length=100)
    
    def __str__(self):
        return self.qid
    
    
    