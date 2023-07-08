from django.db import models

class Craft(models.Model):

    type = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    about = models.TextField(max_length=500)
    verified_craft = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.type

    class Meta:
        ordering = ['type']
