from django.db import models

# Create your models here.
class EngWS(models.Model):
    Chapter = models.CharField(max_length=300)
    EngWSFile = models.FileField(upload_to='EngWS')
    
    def __str__(self):
        return self.Chapter

class HinWS(models.Model):
    Chapter = models.CharField(max_length=300)
    HinWSFile = models.FileField(upload_to='HindiWS')
    
    def __str__(self):
        return self.Chapter

class AraWS(models.Model):
    Chapter = models.CharField(max_length=300)
    AraWSFile = models.FileField(upload_to='ArabicWS')
    
    def __str__(self):
        return self.Chapter

class MatWS(models.Model):
    Chapter = models.CharField(max_length=300)
    MatWSFile = models.FileField(upload_to='MathsWS')
    
    def __str__(self):
        return self.Chapter

class SciWS(models.Model):
    Chapter = models.CharField(max_length=300)
    SciWSFile = models.FileField(upload_to='ScienceWS')
    
    def __str__(self):
        return self.Chapter

class IssWS(models.Model):
    Chapter = models.CharField(max_length=300)
    IssWSFile = models.FileField(upload_to='IndianSSTWS')
    
    def __str__(self):
        return self.Chapter

class UssWS(models.Model):
    Chapter = models.CharField(max_length=300)
    UssWSFile = models.FileField(upload_to='UAESSTWS')
    
    def __str__(self):
        return self.Chapter
