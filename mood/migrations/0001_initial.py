# Generated by Django 3.1.4 on 2020-12-14 02:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Thinker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='name of thinker')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Mood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('mood', models.IntegerField(verbose_name='mood of person')),
                ('thinker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mood.thinker')),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
