# Generated by Django 2.2.13 on 2020-06-25 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_post_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='media/images/'),
        ),
    ]
