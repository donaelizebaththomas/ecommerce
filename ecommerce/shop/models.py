from django.db import models

# Create your models here.

class category(models.Model):
    name=models.CharField(max_length=20)
    desc=models.TextField()
    image=models.ImageField(upload_to='category',null=True,blank=True)

    def __str__(self):
        return self.name

class product(models.Model):
    name = models.CharField(max_length=20)
    desc = models.TextField()
    # price=models.IntegerField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to='product', null=True, blank=True)
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)         #only once or one time
    updated=models.DateTimeField(auto_now=True)             #every time we update records
    Category=models.ForeignKey(category,on_delete=models.CASCADE)
    #on_delete - it will delete the product details when category data will be deleted

    def __str__(self):
        return self.name

