from django.db import models

# Create your models here.
class QueueEntry(models.Model):
    number = models.PositiveIntegerField()
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, blank=True)
    email = models.EmailField(blank=True)
    status = models.CharField(max_length=20, choices=[
        ('waiting', 'Waiting'),
        ('notified', 'Notified'),
        ('served', 'Served'),
        ('cancelled', 'Cancelled'),
    ], default='waiting')
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"#{self.number} - {self.name} ({self.status})"
    
class QueueStatus(models.Model):
    is_open = models.BooleanField(default=True)

