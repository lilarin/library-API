# Generated by Django 5.1 on 2024-08-15 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0004_alter_payment_session_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_type',
            field=models.CharField(choices=[('PAYMENT', 'Payment'), ('FINE', 'Fine')], max_length=24),
        ),
    ]