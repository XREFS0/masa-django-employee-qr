"""
Developed by MASA
All Rights Reserved.
"""

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("eqrApp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="employee",
            name="email",
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
