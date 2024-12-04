# Generated by Django 4.2.11 on 2024-05-31 10:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("license", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="instance",
            name="instance_id",
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.RenameField(
            model_name="instance",
            old_name="version",
            new_name="current_version",
        ),
        migrations.RemoveField(
            model_name="instance",
            name="api_key",
        ),
        migrations.AddField(
            model_name="instance",
            name="domain",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="instance",
            name="latest_version",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name="instance",
            name="product",
            field=models.CharField(default="youtrack-ce", max_length=50),
        ),
        migrations.CreateModel(
            name="ChangeLog",
            fields=[
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Created At"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Last Modified At"
                    ),
                ),
                (
                    "id",
                    models.UUIDField(
                        db_index=True,
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField(blank=True)),
                ("version", models.CharField(max_length=100)),
                ("tags", models.JSONField(default=list)),
                ("release_date", models.DateTimeField(null=True)),
                ("is_release_candidate", models.BooleanField(default=False)),
                (
                    "created_by",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(class)s_created_by",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Created By",
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(class)s_updated_by",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Last Modified By",
                    ),
                ),
            ],
            options={
                "verbose_name": "Change Log",
                "verbose_name_plural": "Change Logs",
                "db_table": "changelogs",
                "ordering": ("-created_at",),
            },
        ),
    ]
