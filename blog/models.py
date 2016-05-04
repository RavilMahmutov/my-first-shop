from django.db import models
from django.utils import timezone 


class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length = 200)
	text = models.TextField()
	create_date = models.DateTimeField(default = timezone.now)
	published_date = models.DateTimeField(blank = True, null = True)
	image = models.ImageField(upload_to = 'images', null = True, blank = True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title


class Comment(models.Model):
	post = models.ForeignKey('blog.Post', related_name = 'comments')
	author = models.ForeignKey('auth.User')
	text = models.TextField()
	created_date = models.DateTimeField(default = timezone.now)
	approved_comment = models.BooleanField(default = False)

	def approve(self):
		self.approved_comment = True
		self.save()

	def __str__(self):
		return self.text





#модели товров и категорий
class Good(models.Model):
	title = models.CharField(max_length = 200)
	description = models.TextField()
	factory = models.CharField(max_length = 200)
	price = models.IntegerField()
	image = models.ImageField(upload_to = 'images/goods', null = True, blank = True)
	category = models.ForeignKey('blog.Category', related_name = 'goods')
	
	def __str__(self):
		return self.title

class Category(models.Model):
	title = models.CharField(max_length = 200)
	image = models.ImageField(upload_to = 'images/categories', null = True, blank = True)
	
	def __str__(self):
		return self.title

