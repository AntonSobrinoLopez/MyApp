# Generated by Django 4.1.5 on 2023-01-16 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_alter_member_joind_date_alter_member_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='joind_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='married',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
