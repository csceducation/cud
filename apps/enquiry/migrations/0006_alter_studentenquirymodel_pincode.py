# Generated by Django 5.0.3 on 2024-03-19 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("enquiry", "0005_alter_studentenquirymodel_enquiry_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="studentenquirymodel",
            name="pincode",
            field=models.IntegerField(
                blank=True, default=None, null=True, verbose_name="Pincode"
            ),
        ),
    ]
