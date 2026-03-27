from django.db import models

# Create your models here.
'''
django models fields:
    -html widget
    -validation 
    -db size 
CharField: for short text, requires max_length
TextField: for long text, no max_length required
IntegerField: for integers
FloatField: for floating-point numbers  
DateField: for dates
DateTimeField: for date and time
BooleanField: for true/false values
ForeignKey: for relationships between models (e.g., one-to-many)
ManyToManyField: for many-to-many relationships
OneToOneField: for one-to-one relationships 
'''
def image_upload(instance, filename):
    imagename, extention = filename.split('.')
    return "jobs/%s.%s" % (instance.id,extention)

JOB_TYPE = (
    ('full-time', 'Full Time'),
    ('part-time', 'Part Time')
    )
    
class Category(models.Model):
        name = models.CharField(max_length=100)
        def __str__(self):
            return self.name

class Job(models.Model): #table
    title = models.CharField(max_length=100) #column
    description = models.TextField()
    job_type = models.CharField(max_length=15, choices=JOB_TYPE, default='full-time')
    # location = models.CharField(max_length=100)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to=image_upload, null=True , blank=True)
    
    
    def __str__(self):
        return self.title
