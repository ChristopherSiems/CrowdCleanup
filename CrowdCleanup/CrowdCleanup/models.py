from django.db import models

class Pin(models.Model):
  STATUS_OPTIONS = (
    ('to_be_cleaned', 'TO BE CLEANED'),
    ('cleaned', 'CLEANED')
  )

  lat = models.FloatField()
  long = models.FloatField()
  date = models.DateTimeField(auto_now_add=True)
  description = models.TextField()
  image = models.ImageField(upload_to='media/', null=True, blank=True)
  status = models.CharField(choices=STATUS_OPTIONS, default="to_be_cleaned")
  description = models.TextField()
