# Generated by Django 3.1.3 on 2020-11-20 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0011_auto_20201118_0839'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='nested_messages',
            field=models.ManyToManyField(blank=True, null=True, related_name='resent_messages', to='chats.Message'),
        ),
    ]
