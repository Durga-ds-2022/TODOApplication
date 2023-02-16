from django.db import models

# Create your models here.
class Todo(models.Model):
    name= models.CharField(max_length= 100)
    is_completed= models.BooleanField(default=False)
    create_at= models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    