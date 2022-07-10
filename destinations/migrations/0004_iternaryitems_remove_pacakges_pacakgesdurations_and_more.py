# Generated by Django 4.0.6 on 2022-07-09 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0003_delete_demo'),
    ]

    operations = [
        migrations.CreateModel(
            name='IternaryItems',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='destinations.basemodel')),
                ('Title', models.CharField(max_length=100)),
                ('Day', models.DateField()),
            ],
            bases=('destinations.basemodel',),
        ),
        migrations.RemoveField(
            model_name='pacakges',
            name='PacakgesDurations',
        ),
        migrations.AddField(
            model_name='pacakges',
            name='PackagesInclusion',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pacakges',
            name='PackgesDurations',
            field=models.DurationField(blank=True, null=True),
        ),
    ]
