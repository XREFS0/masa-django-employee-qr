"""
Developed by MASA
All Rights Reserved.
"""

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("eqrApp", "0003_remove_employee_qr_path"),
    ]

    operations = [
        migrations.AddField(
            model_name="employee",
            name="avatar",
            field=models.ImageField(blank=True, null=True, upload_to="employee-avatars/"),
        ),
    ]
