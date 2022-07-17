from django.db import models
from .tracking import checker

# Create your models here.

class amaze(models.Model):
    name=models.CharField(max_length=220,blank=True)
    url=models.URLField()
    curr_val=models.FloatField(blank=True)
    exp_val=models.FloatField(default=0)
    differ=models.FloatField(default=0)
    modified=models.DateField(auto_now=True)
    created=models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering=('differ','-created')
    
    def save(self, *args, **kwargs):

        name,price=checker(self.url)
        old_price=self.exp_val
        if self.curr_val:
            if price!=old_price:
               old_price=self.exp_val
               diff=price-old_price
               self.differ=round(diff,2)
            else:
                self.differ=0
            
            
        self.name=name
        self.curr_val=price
        super().save(*args, **kwargs)


