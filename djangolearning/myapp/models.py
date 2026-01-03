from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class ChaiVariety(models.Model):
    CHAI_TYPES_CHOICE=[
        ('ML','MASALA'),
        ('GR','GINGER'),
        ('KL','KIWI'),
        ('PL','PLAIN'),
        ('EL','ELACHI')

    ]
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='chais/')
    date_added=models.DateTimeField(default=timezone.now)
    type=models.CharField(max_length=2,choices=CHAI_TYPES_CHOICE)
    description=models.TextField(default='')

    def __str__(self):
        return self.name
    
# one to many

# class ChaiReview(models.Model):
#     chai = models.ForeignKey(ChaiVariety,on_delete=models.CASCADE, related_name='name')
#     user=models.ForeignKey(User,on_delete=models.CASCADE)
#     rating=models.IntegerField()
#     comment=models.TextField()
#     date_added=models.DateTimeField(default=timezone.now)

#     def __str__(self):
#         return f'{self.user.username} review for {self.chai.name}'


# many to many 

# class Stores(models.Model):
#     name=models.CharField(max_length=100)
#     location=models.CharField(max_length=100)
#     chai_variety=models.ManyToManyField(ChaiVariety, related_query_name='stores')

#     def __str__(self):
#         return self.name
    
# one to one field

# class ChaiCertificate(models.Model):
#     chai=models.OneToOneField(ChaiVariety,on_delete=models.CASCADE,related_name='certificate')
#     certificate_number=models.CharField(max_length=100)
#     issues_date=models.DateField(default=timezone.now)
#     valid_until=models.DateTimeField()

#     def __str__(self):
#         return f'Certificate for {self.name.chai}'