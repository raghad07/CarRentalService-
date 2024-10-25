# Generated by Django 4.2.16 on 2024-10-24 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('payment', '0001_initial'),
        ('datetimeapp', '0001_initial'),
        ('brands', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_pickup_time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pickup_times', to='datetimeapp.mydata')),
                ('booking_return_time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='return_times', to='datetimeapp.mydata')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brands.car')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.personaldetails')),
            ],
        ),
    ]
