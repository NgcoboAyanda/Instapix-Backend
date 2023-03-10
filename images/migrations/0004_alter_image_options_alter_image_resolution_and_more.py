# Generated by Django 4.1.4 on 2022-12-16 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0003_image_likes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['id']},
        ),
        migrations.AlterField(
            model_name='image',
            name='resolution',
            field=models.CharField(choices=[('small', '256x256'), ('medium', '512x512'), ('large', '1024x1024')], max_length=100),
        ),
        migrations.AlterField(
            model_name='image',
            name='url',
            field=models.CharField(max_length=2000),
        ),
    ]
