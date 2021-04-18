from django.db import models

# Create your models here.
class EngClassNotes(models.Model):
    Chapter = models.CharField(max_length=300)
    EngNotesFile = models.FileField(upload_to='Eng_Notes')
    
    def __str__(self):
        return self.Chapter

class HinClassNotes(models.Model):
    Chapter = models.CharField(max_length=300)
    HinNotesFile = models.FileField(upload_to='Hin_Notes')
    
    def __str__(self):
        return self.Chapter


class AraClassNotes(models.Model):
    Chapter = models.CharField(max_length=300)
    AraNotesFile = models.FileField(upload_to='Arabic_Notes')
    
    def __str__(self):
        return self.Chapter

class MatClassNotes(models.Model):
    Chapter = models.CharField(max_length=300)
    MatNotesFile = models.FileField(upload_to='Maths_Notes')
    
    def __str__(self):
        return self.Chapter

class SciClassNotes(models.Model):
    Chapter = models.CharField(max_length=300)
    SciNotesFile = models.FileField(upload_to='Science_Notes')
    
    def __str__(self):
        return self.Chapter

class IssClassNotes(models.Model):
    Chapter = models.CharField(max_length=300)
    IssNotesFile = models.FileField(upload_to='Indian_SST_Notes')
    
    def __str__(self):
        return self.Chapter

class UssClassNotes(models.Model):
    Chapter = models.CharField(max_length=300)
    UssNotesFile = models.FileField(upload_to='UAE_SST_Notes')
    
    def __str__(self):
        return self.Chapter
