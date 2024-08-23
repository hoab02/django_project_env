# models.py
from django.db import models

class Robot(models.Model):
    robot_id = models.CharField(max_length=100, unique=True)
    position_id = models.CharField(max_length=100)
    orientation = models.CharField(max_length=100)

    def __str__(self):
        return self.robot_id
