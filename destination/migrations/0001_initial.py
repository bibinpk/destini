# Generated by Django 3.1.2 on 2020-10-16 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Name')),
                ('place', models.CharField(max_length=50, verbose_name='Place')),
                ('route_road', models.CharField(max_length=100, verbose_name='By road')),
                ('route_air', models.CharField(max_length=100, verbose_name='By air')),
                ('route_rail', models.CharField(max_length=100, verbose_name='By rail')),
                ('best_time', models.TextField(verbose_name='Best time for visit')),
                ('Things_to_do', models.TextField(verbose_name='Things to do')),
                ('type', models.CharField(max_length=200, verbose_name='Type')),
                ('image', models.ImageField(upload_to='pics', verbose_name='Picture')),
            ],
            options={
                'verbose_name': 'Destination',
                'verbose_name_plural': 'Destinations',
            },
        ),
        migrations.CreateModel(
            name='districts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name': 'District',
                'verbose_name_plural': 'Districts',
            },
        ),
        migrations.CreateModel(
            name='popular',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='destination.destination')),
            ],
            options={
                'verbose_name': 'Popular',
                'verbose_name_plural': 'Popular',
            },
        ),
        migrations.AddField(
            model_name='destination',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='destination.districts'),
        ),
    ]
