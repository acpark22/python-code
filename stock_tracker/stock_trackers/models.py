from django.db import models
# Create your models here.

class Stock(models.Model):
    """ A stock the user is tracking."""
    text= models.CharField(max_length=50)
    date_added= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ Return a string representation of the model."""
        return self.text

class Entry(models.Model):
    """Any notes to be added about the stock."""
    stock= models.ForeignKey(Stock, on_delete= models.CASCADE)
    text= models.TextField()
    date_added= models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural= 'entries'

    def __str__(self):
        """Return a string representation of the model."""
        
        return f"{self.text[:50]}..."


