# Generated by Django 4.2.7 on 2024-01-25 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_alter_author_date_of_death'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='born'),
        ),
    ]
