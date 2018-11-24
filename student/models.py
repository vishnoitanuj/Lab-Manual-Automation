from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db.models.signals import post_save
from django.urls import reverse

# Create your models here.
class UserProfile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	first_name=models.CharField(max_length=100,default='')
	last_name=models.CharField(max_length=100,default='')
    #profile_image=models.FileField(null=True,blank=True)
	#user_type=models.CharField(max_length=4,choices=USER_TYPE_CHOICES)
	USER_YEAR_CHOICES=(('1st','1st Year Student'),('2nd','2nd Year Student'),('3rd','Third Year Student'),('4th','4th Year Student'),('phd','PHD'),('fac','Faculty'))
	user_year=models.CharField(max_length=3,choices=USER_YEAR_CHOICES,default='1st')
	#current_cgpa=models.FloatField(validators = [MinValueValidator(0), MaxValueValidator(10)],null=True)


	def __str__(self):
		return str(self.user.username)

	def get_absolute_url(self):
		return reverse('student-detail',args=[str(self.id)])

def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile=UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile,sender=User)

class Assignment(models.Model):
	author=models.ForeignKey("UserProfile", on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, help_text='Enter assignment number(e.g. Experiment 1)')
    aim = models.CharField(max_length=500, default='Perform the following')
	timestamp=models.DateTimeField(auto_now=False,auto_now_add=True)
   class Meta:
		ordering = ["-timestamp"]
	def get_absolute_url(self):	
		return reverse('blog-detail',args=[str(self.id)])

	def __str__(self):
		return (self.name)
class Work(models.Model):
    title = models.ForeignKey('Assignment',on_delete=models.SET_NULL, null=True)
    upload_data = models.DateTimeField(auto_now_add=True, blank=True)
    deadline = models.DateTimeField(blank=True, null=True)
    pdf =  models.FileField(null=True, blank=True, validators=[FileExtensionValidator(['pdf'])])
