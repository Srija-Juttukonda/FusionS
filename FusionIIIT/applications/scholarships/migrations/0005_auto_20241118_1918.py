# Generated by Django 3.1.5 on 2024-11-18 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarships', '0004_auto_20241118_1917'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='director_gold',
            name='nearest_railwaystations',
        ),
        migrations.AlterField(
            model_name='director_gold',
            name='nearest_railwaystation',
            field=models.CharField(max_length=25, null=True),
        ),
    ]
