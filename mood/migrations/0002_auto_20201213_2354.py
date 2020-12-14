# Generated by Django 3.1.4 on 2020-12-14 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mood', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mood',
            name='thinker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='moods', to='mood.thinker'),
        ),
        migrations.AlterUniqueTogether(
            name='thinker',
            unique_together={('name',)},
        ),
    ]
