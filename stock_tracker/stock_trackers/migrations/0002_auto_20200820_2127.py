# Generated by Django 3.1 on 2020-08-20 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock_trackers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='date_added',
        ),
        migrations.AlterField(
            model_name='stock',
            name='text',
            field=models.CharField(max_length=50),
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock_trackers.stock')),
            ],
            options={
                'verbose_name_plural': 'entries',
            },
        ),
    ]
