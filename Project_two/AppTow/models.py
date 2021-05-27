from django.db import models

# Create your models here.

class Topic(models.Model):
    top_name = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    topic = models.ForeignKey(Topic)
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name 

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage)
    date = models.DateField()


    def __str__(self):
        return str(self.date )




class Author(models.Model):
	name = models.CharField(max_length = 30)
	id = models.IntegerField(primary_key=True)
	

	def __str__(self):
		return self.name

class Book(models.Model):
	title = models.CharField(max_length = 100)
	author = models.ForeignKey(Author, on_delete = models.CASCADE)

	def __str__(self):
		return self.title
