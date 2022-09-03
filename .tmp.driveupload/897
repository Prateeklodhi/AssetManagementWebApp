from django.db import models
# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100,null=True,blank=False)
    types = (
        ("Doctor","Doctor"),
        ("Technical Helpdesk","Technical Helpdesk"),
        ("Helpdest","Helpdesk"),
        ("Management Information System","Management Information System"),
        )
    employee_id = models.CharField(primary_key=True,max_length=100,blank=False,null=False,unique=True)
    employee_type = models.CharField(choices=types,max_length=50,default="Not Selected")
    def __str__(self) -> str:
        return self.name
    class Meta:
        ordering  = ['name']


class Asset(models.Model):
    status = (
        ('Alloted','Alloted'),
        ('Unalloted','Unalloted')
    )
    category = (
        ("Electronic","Electronic"),
        ("Stationary","Stationary"),
        ("Furniture","Furniture"),
        ("Appliances","Appliances"),
        )
    asset_name = models.CharField(max_length=150,null=True)
    asset_serial_number = models.CharField(max_length=50,primary_key=True,null=False,blank=False)
    asset_category = models.CharField(choices=category,null =True,max_length=50)
    asset_host_id= models.CharField(max_length=100,null=True)
    vendor_name = models.CharField(null = True,blank=True,max_length=150)
    purchase_date = models.DateField(null = True,blank=True)
    invoice = models.FileField(upload_to="invoice/",null=True,blank=True)
    issued_to = models.ForeignKey(Employee,on_delete=models.SET_NULL,null= True,blank=True,default="None")
    issue_date = models.DateField(null=True,blank=True)
    asset_status = models.CharField(choices=status,max_length=15,null = True,default="Unalloted")
    def __str__(self) -> str:
        return self.asset_name

    class Meta:
        ordering = ['asset_name']

