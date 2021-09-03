from django.db import models
#class data_config:
 #   ib:int 
#choices= (("PENDING",'0'), ("0","BOUGHT"), ("0","NOT AVAILABLE"))

class grocery_item(models.Model):
    item_name=models.CharField(max_length=200,default='default')
    item_quantity=models.CharField(max_length=120)
    item_status=models.CharField(max_length=100,default=0)
    item_date=models.DateField()
    user_name=models.CharField(max_length=100,default='default')
# Create your models here.
