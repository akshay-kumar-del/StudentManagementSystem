
from django.db import models

class Student(models.Model):
    student_name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.PositiveIntegerField(null=True, blank=True)
    mobile_number = models.CharField(max_length=15)
    profile_image = models.ImageField(
        upload_to='student_images/',
        null=True,
        blank=True
    )
    course = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student_name