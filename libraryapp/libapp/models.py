from django.db import models
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save
from datetime import datetime

# Create your models here.
class Books(models.Model):
	book_title = models.CharField(max_length=200)
	date_of_pub = models.DateField()
	isbn_number = models.IntegerField(default=0)
	book_author = models.CharField(max_length=200)
	book_category = models.CharField(max_length=20)
	qty_in_lib = models.IntegerField(default=0)
	# qty_available = models.IntegerField(default=0)

	def __unicode__(self):
		return self.book_title

	def available_books(self):
		return self.qty_in_lib - self.book_user_map.all().count()

class AdditionalDetails(models.Model):
	user = models.OneToOneField(User)
	is_librarian = models.BooleanField(default = False)
	is_valid = models.BooleanField(default = False)
	
class BookUserMap(models.Model):
	user = models.ForeignKey(User)
	book = models.ForeignKey('Books', related_name = "book_user_map")
	issue_date = models.DateField(default=datetime.now())
	return_date = models.DateField(blank=True, null=True)
	days = models.IntegerField(default=7)
	fine = models.IntegerField(default=0)
	book_returned = models.BooleanField(default=False)