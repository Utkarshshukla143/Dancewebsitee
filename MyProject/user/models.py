from django.db import models


# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=120)
    contact = models.CharField(max_length=20)
    message = models.CharField(max_length=600)

    def __str__(self):
        return self.email


class category(models.Model):
    cname = models.CharField(max_length=40)
    cpic = models.ImageField(upload_to='static/category/', default="")
    cdate = models.DateField()

    def __str__(self):
        return self.cname


class profile(models.Model):
    name = models.CharField(max_length=120)
    mobile = models.CharField(max_length=20)
    email = models.EmailField(max_length=80, primary_key=True)
    passwd = models.CharField(max_length=20)
    ppic = models.ImageField(upload_to='static/profile/', default="")
    address = models.TextField(max_length=300)


class signup(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField(max_length=100)
    gender = models.CharField(max_length=100)
    mobile = models.CharField(max_length=20)
    email = models.CharField(max_length=120)
    password = models.CharField(max_length=20)
    profession = models.CharField(max_length=50)
    college = models.CharField(max_length=200)
    profile = models.ImageField(upload_to='static/profilepic/', default="")
    status = models.BooleanField()
    RegDate = models.DateField()

    def __str__(self):
        return self.email


class blogdetail(models.Model):
    authorid = models.CharField(max_length=200)
    blogcategory = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    attechment = models.ImageField(upload_to='static/document/', default="")
    thumbnail = models.ImageField(upload_to='static/thumbnail/', default="")
    blogdate = models.DateField(max_length=100)

    def __str__(self):
        return self.title


class signin(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class createblogs(models.Model):
    topic = models.CharField(max_length=100)
    discription = models.CharField(max_length=600)
    document = models.ImageField(upload_to='static/document/', default="")
    thumbnail = models.ImageField(upload_to='static/thumbnail/', default="")

    def __str__(self):
        return self.topic
