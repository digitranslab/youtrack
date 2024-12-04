# Generated by Django 4.2.11 on 2024-08-29 09:40

import django.core.validators
from django.db import migrations, models
import youtrack.db.models.asset


class Migration(migrations.Migration):

    dependencies = [
        ("db", "0074_deploy_board_and_project_issues"),
    ]

    operations = [
        migrations.AlterField(
            model_name="fileasset",
            name="asset",
            field=models.FileField(
                upload_to=youtrack.db.models.asset.get_upload_path,
                validators=[
                    django.core.validators.FileExtensionValidator(
                        allowed_extensions=["jpg", "jpeg", "png"]
                    ),
                    youtrack.db.models.asset.file_size,
                ],
            ),
        ),
    ]
