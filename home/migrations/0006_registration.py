# Generated by Django 4.2.1 on 2023-10-08 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_contact_age_alter_contact_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=122)),
                ('lastname', models.CharField(max_length=122)),
                ('email', models.EmailField(max_length=254)),
                ('country', models.CharField(max_length=122)),
                ('course', models.CharField(max_length=122)),
                ('gender', models.CharField(max_length=122)),
                ('age', models.CharField(max_length=122)),
                ('payment_method', models.CharField(max_length=122)),
                ('date', models.DateField()),
            ],
        ),
    ]
