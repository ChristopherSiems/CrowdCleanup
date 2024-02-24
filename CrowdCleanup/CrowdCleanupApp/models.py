from django.db import models

class Pin(models.Model):
  lat = models.FloatField()
  long = models.FloatField()
  date = models.DateTimeField(auto_now_add=True)
  description = models.TextField()
  image = models.ImageField(upload_to='media/', null=True, blank=True)
<<<<<<< Updated upstream:CrowdCleanup/CrowdCleanupApp/models.py
  status = models.CharField(choices=STATUS_OPTIONS, default="to_be_cleaned", max_length = 13)
=======
  status = models.CharField( default='TO BE CLEANED', max_length = 13)
>>>>>>> Stashed changes:CrowdCleanup/CrowdCleanup/models.py
  description = models.TextField()
