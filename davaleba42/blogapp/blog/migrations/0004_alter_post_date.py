# Generated by Django 5.0.6 on 2024-06-04 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
