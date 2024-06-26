from django.db import models

# Create your models here.


class File(models.Model):
    niveau_choix=[
        ('CE1', 'CE1'),
        ('CE2', 'CE2'),
        ('CM1', 'CM1'),
        ('CM2', 'CM2'),
        ('6eme', ' 6ème'),
        ('5eme', '5ème'),
        ('4eme', '4ème'),
        ('3eme', '3ème'),
    ]
    matiere_choix = [
        ('Maths', 'Mathematics'),
        ('Physique-Chimie', 'Physics'),
        ('Anglais', 'Chemistry'),
        ('Français', 'French'),
        ('Histoire-Geo', 'History-Geography'),
        ('SVT', 'Life Sciences'),
        ('EPS', 'Physical Education'),
        ('Sciences', ' Science'),
    ]


    niveau = models.CharField(null=True,choices=niveau_choix)
    matiere = models.CharField(null=True,choices=matiere_choix)
    caption = models.CharField(max_length=100)
    file = models.FileField(null=True, editable=True)
   #file = models.BinaryField(null=True, editable=True)
    def __str__(self):
        return self.caption


