# Generated by Django 4.1 on 2022-10-26 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Repo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matric_no', models.CharField(max_length=6)),
                ('project_title', models.CharField(max_length=200)),
                ('year', models.IntegerField(max_length=4)),
                ('document', models.FileField(upload_to='')),
            ],
        ),
    ]
