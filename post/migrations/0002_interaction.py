# Generated by Django 4.2.13 on 2024-06-22 16:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interaction',
            fields=[
                ('interaction_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('interaction_type', models.CharField(max_length=50)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('post', models.ManyToManyField(related_name='interactions', to='post.post')),
                ('user', models.ManyToManyField(related_name='interactions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
