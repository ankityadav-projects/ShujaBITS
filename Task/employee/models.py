from django.db import models


class Emp(models.Model):
    name=models.CharField(max_length=25)
    email=models.CharField(max_length=25)
    doj=models.DateField()
    location=models.CharField(max_length=25,choices=(("Mumbai",'Mumbai'),("Pune",'Pune'),("Delhi",'Delhi'),("Bangalore",'Bangalore')))

    class Meta:
        db_table="employee"
