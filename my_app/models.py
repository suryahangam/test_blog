from django.db import models

class Experience(models.Model):
    
    title = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    company_name = models.CharField(max_length=10)
    cover_image = models.ImageField(null=True)

    def __str__(self):
        return self.title
    

