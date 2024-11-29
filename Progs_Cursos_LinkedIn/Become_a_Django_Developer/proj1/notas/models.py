from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Nota(models.Model):
    # First add title
    title = models.CharField(max_length=300)
    
    # Then add description
    description = models.TextField()
    
    # And finally, add a publication date
    created_at = models.DateTimeField(auto_now_add=True)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sobre")