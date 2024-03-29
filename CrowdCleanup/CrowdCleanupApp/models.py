from django.db import models

class Pin(models.Model):
  lat = models.FloatField()
  long = models.FloatField()
  zipcode = models.CharField(max_length = 5, default = '00000')
  date = models.DateTimeField(auto_now_add=True)
  description = models.TextField()
  image = models.ImageField(upload_to='media/', null=True, blank=True)
  status = models.CharField( default='TO BE CLEANED', max_length = 13)
