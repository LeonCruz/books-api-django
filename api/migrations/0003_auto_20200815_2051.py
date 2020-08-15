# Generated by Django 3.1 on 2020-08-15 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_author_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='pages',
        ),
        migrations.AlterField(
            model_name='books',
            name='author',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='books',
            name='category',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]