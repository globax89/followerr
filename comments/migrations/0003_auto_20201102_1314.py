# Generated by Django 3.1.1 on 2020-11-02 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photoalbums', '0003_auto_20201102_1155'),
        ('posts', '0002_auto_20201030_1409'),
        ('comments', '0002_auto_20201030_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='picture',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='picture_comments', to='photoalbums.image'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_comments', to='posts.post'),
        ),
    ]
