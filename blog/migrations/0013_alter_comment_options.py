# Generated by Django 4.1 on 2022-08-22 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_date'], 'verbose_name': 'کامنت', 'verbose_name_plural': 'کامنت ها'},
        ),
    ]
