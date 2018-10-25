from django.db import models

# Create your models here.
# Create my tabel in here

# inherite the models.Model
class Class(models.Model):
    gname = models.CharField(max_length=20)
    gdate = models.DateField()
    gBoyNum = models.IntegerField()
    gGrilNum = models.IntegerField()
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.gname

class Student(models.Model):
    sName = models.CharField(max_length=20)
    sGender = models.BooleanField(default=True) # because there are only two choose, male is True
    sAge = models.IntegerField()
    sSummary = models.CharField(max_length=500)
    sClass = models.ForeignKey(to='Class',on_delete=None) # the the foreign key
    sScore = models.IntegerField()
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.sName


