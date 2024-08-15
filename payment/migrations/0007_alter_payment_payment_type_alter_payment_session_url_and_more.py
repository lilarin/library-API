# Generated by Django 4.2.11 on 2024-08-15 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("payment", "0006_alter_payment_payment_type_alter_payment_session_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payment",
            name="payment_type",
            field=models.CharField(
                choices=[("PAYMENT", "Payment"), ("FINE", "Fine")], max_length=7
            ),
        ),
        migrations.AlterField(
            model_name="payment",
            name="session_url",
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="payment",
            name="status",
            field=models.CharField(
                choices=[("PENDING", "Pending"), ("PAID", "Paid")], max_length=7
            ),
        ),
    ]