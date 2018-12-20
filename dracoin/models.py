from django.db import models

class Article(models.Model):
	title = models.CharField(max_length=200, db_index=True)
	slug = models.SlugField(max_length=200, unique=True)
	content = models.TextField(blank=True, max_length=2000, db_index=True)
	author = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published', auto_now_add=True)
	def __str__(self):
		return self.title

class Tag(models.Model):
	title = models.CharField(max_length=200, unique=True)
	def __str__(self):
		return self.title

class Image(models.Model):
	title = models.CharField(max_length=200)
	image = models.ImageField(upload_to='pictures')
	def __str__(self):
		return self.title

class Comment(models.Model):
	name = models.CharField(max_length=200)
	email = models.EmailField(max_length=200)
	content = models.TextField(max_length=500, db_index=True)
	root = models.ForeignKey(Article, on_delete=models.CASCADE)
	previous = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
	pub_date = models.DateTimeField('date published', auto_now_add=True)
	def __str__(self):
		return self.content