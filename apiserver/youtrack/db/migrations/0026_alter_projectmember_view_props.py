# Generated by Django 3.2.18 on 2023-04-04 21:50

from django.db import migrations, models
import youtrack.db.models.project


class Migration(migrations.Migration):
    dependencies = [
        ("db", "0025_auto_20230331_0203"),
    ]

    operations = [
        migrations.AlterField(
            model_name="projectmember",
            name="view_props",
            field=models.JSONField(
                default=youtrack.db.models.project.get_default_props
            ),
        ),
    ]
