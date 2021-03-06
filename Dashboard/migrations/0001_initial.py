# Generated by Django 2.1.2 on 2018-11-01 21:59

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dayOfWeek', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(6)])),
                ('h0600', models.BooleanField(default=False)),
                ('h0700', models.BooleanField(default=False)),
                ('h0800', models.BooleanField(default=False)),
                ('h0900', models.BooleanField(default=False)),
                ('h1000', models.BooleanField(default=False)),
                ('h1100', models.BooleanField(default=False)),
                ('h1200', models.BooleanField(default=False)),
                ('h1300', models.BooleanField(default=False)),
                ('h1400', models.BooleanField(default=False)),
                ('h1500', models.BooleanField(default=False)),
                ('h1600', models.BooleanField(default=False)),
                ('h1700', models.BooleanField(default=False)),
                ('h1800', models.BooleanField(default=False)),
                ('h1900', models.BooleanField(default=False)),
                ('h2000', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CourseOffer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=50, verbose_name='Course Number')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employeeId', models.CharField(max_length=50, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator('Y00\\d{6}', 'Employee ID does not match the specified format')], verbose_name='Y Number')),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, verbose_name='Sex')),
                ('dob', models.DateField(verbose_name='Date of Birth')),
                ('created', models.DateField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startTime', models.DateTimeField(auto_now_add=True)),
                ('endTime', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='courseoffer',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dashboard.Employee'),
        ),
    ]
