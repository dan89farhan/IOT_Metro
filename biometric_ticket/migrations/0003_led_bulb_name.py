# Generated by Django 2.0.3 on 2018-03-24 18:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('biometric_ticket', '0002_led_bulb'),
    ]

    operations = [
        migrations.AddField(
            model_name='led_bulb',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
