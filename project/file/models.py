from django.db import models

# Create your models here.


class File(models.Model):
    niveau_choix=[
        ('CE1', 'Classe de CE1'),
        ('CE2', 'Classe de CE2'),
        ('CM1', 'Classe de CM1'),
        ('CM2', 'Classe de CM2'),
        ('6eme', 'Classe de 6ème'),
        ('5eme', 'Classe de 5ème'),
        ('4eme', 'Classe de 4ème'),
        ('3eme', 'Classe de 3ème'),
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
    file = models.BinaryField(null=True, editable=True)
    def __str__(self):
        return self.caption


