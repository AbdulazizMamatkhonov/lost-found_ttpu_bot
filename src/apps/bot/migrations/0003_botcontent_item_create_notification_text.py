# Generated by Django 4.1.1 on 2022-10-27 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0002_botcontent_item_photo_exception_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='botcontent',
            name='item_create_notification_text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
