# Generated by Django 4.1.3 on 2022-12-04 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0002_parent_register_approval_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hostel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostel_name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('Fee_details', models.CharField(max_length=25)),
                ('total_rooms', models.IntegerField()),
                ('room_facilities', models.CharField(max_length=250)),
                ('contact_number', models.IntegerField()),
                ('hostel_image', models.ImageField(upload_to='image')),
            ],
        ),
    ]