"""
Developed by MASA
All Rights Reserved.
"""

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("eqrApp", "0002_employee_email"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="employee",
            name="qr_path",
        ),
    ]
