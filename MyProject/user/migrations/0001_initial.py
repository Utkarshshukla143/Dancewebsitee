# Generated by Django 3.2.4 on 2021-10-05 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blogdetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authorid', models.CharField(max_length=200)),
                ('blogcategory', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('attechment', models.ImageField(default='', upload_to='static/document/')),
                ('thumbnail', models.ImageField(default='', upload_to='static/thumbnail/')),
                ('blogdate', models.DateField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=40)),
                ('cpic', models.ImageField(default='', upload_to='static/category/')),
                ('cdate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=120)),
                ('contact', models.CharField(max_length=20)),
                ('message', models.CharField(max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='createblogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=100)),
                ('discription', models.CharField(max_length=600)),
                ('document', models.ImageField(default='', upload_to='static/document/')),
                ('thumbnail', models.ImageField(default='', upload_to='static/thumbnail/')),
            ],
        ),
        migrations.CreateModel(
            name='profile',
            fields=[
                ('name', models.CharField(max_length=120)),
                ('mobile', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=80, primary_key=True, serialize=False)),
                ('passwd', models.CharField(max_length=20)),
                ('ppic', models.ImageField(default='', upload_to='static/profile/')),
                ('address', models.TextField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='signin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=120)),
                ('password', models.CharField(max_length=20)),
                ('profession', models.CharField(max_length=50)),
                ('college', models.CharField(max_length=200)),
                ('profile', models.ImageField(default='', upload_to='static/profilepic/')),
                ('status', models.BooleanField()),
                ('RegDate', models.DateField()),
            ],
        ),
    ]