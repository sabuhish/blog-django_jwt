# Generated by Django 2.1.4 on 2018-12-18 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0004_content_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('twitter', models.URLField(blank=True, null=True)),
                ('facebook', models.URLField(blank=True, null=True)),
                ('github', models.URLField(blank=True, null=True)),
                ('copyright', models.CharField(max_length=255)),
            ],
        ),
    ]
