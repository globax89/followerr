# Generated by Django 3.1.3 on 2020-11-17 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0009_remove_chat_to_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='last_message',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='last_chat_message', to='chats.message'),
        ),
        migrations.AlterField(
            model_name='chat',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='group_avatars', verbose_name='Add chat avatar'),
        ),
    ]
