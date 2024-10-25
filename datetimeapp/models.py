from django.db import models



class MyData(models.Model):
    start_time = models.DateTimeField()
    return_time = models.DateTimeField()
    

    def __str__(self):
        return f"Reservation from {self.start_time} to {self.return_time}"
    

    def number_of_days(self):
        duration = self.return_time - self.start_time
        return duration.days + 1  


