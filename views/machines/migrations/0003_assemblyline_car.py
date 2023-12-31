# Generated by Django 4.2.4 on 2023-09-29 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0002_article_photo_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssemblyLine',
            fields=[
                ('machine_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='machines.machine')),
                ('max_capacity', models.IntegerField()),
            ],
            bases=('machines.machine',),
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('machine_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='machines.machine')),
                ('max_speed', models.IntegerField()),
            ],
            bases=('machines.machine',),
        ),
    ]
