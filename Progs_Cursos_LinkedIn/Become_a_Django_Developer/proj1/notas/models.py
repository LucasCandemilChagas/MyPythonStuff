from django.db import models

# Create your models here.
class Nota(models.Model):
    # First add title
    title = models.CharField(max_length=300)
    
    # Then add description
    description = models.TextField()
    
    # And finally, add a publication date
    created_at = models.DateTimeField(auto_now_add=True)