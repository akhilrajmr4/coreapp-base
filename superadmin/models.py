from django.db import models

# Create your models here.

class Branch(models.Model):
    Name = models.CharField(max_length=240)
    Location = models.CharField(max_length=240)

    def __str__(self):
        return self.Name


class Branch_manager(models.Model):
    Branch = models.ForeignKey(Branch, on_delete=models.DO_NOTHING)
    Name = models.CharField(max_length=240)
    Emp_id = models.CharField(max_length=240)
    Email = models.EmailField()
    Phone = models.CharField(max_length=12) 

    def __str__(self):
        return self.Name



class Branch_department(models.Model):
    Branch = models.ForeignKey(Branch, on_delete=models.DO_NOTHING)
    Department_name = models.CharField(max_length=240)