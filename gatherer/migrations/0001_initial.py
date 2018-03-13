# Generated by Django 2.0 on 2018-03-13 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appliance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appliance_id', models.CharField(max_length=45, unique=True)),
                ('appliance_status', models.CharField(choices=[('y', 'On'), ('n', 'Off')], max_length=1)),
                ('last_appliance_energy_consumed', models.FloatField(null=True)),
                ('last_reading_time', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Appliance_Reading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reading_time', models.DateField(unique=True)),
                ('appliance_energy_consumed', models.FloatField(null=True)),
                ('appliance_id', models.ForeignKey(max_length=45, on_delete=django.db.models.deletion.CASCADE, to='gatherer.Appliance')),
            ],
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building_id', models.IntegerField(unique=True)),
                ('city', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=45)),
                ('postcode', models.CharField(max_length=45)),
                ('country', models.CharField(max_length=45)),
                ('nr_Of_Floors', models.IntegerField()),
                ('building_name', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Flat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flat_id', models.CharField(max_length=45, unique=True)),
                ('floor_nr', models.IntegerField()),
                ('time_created', models.DateField()),
                ('time_updated', models.DateField()),
                ('type', models.CharField(max_length=45)),
                ('nr_of_people', models.IntegerField()),
                ('flat_rating', models.FloatField(null=True)),
                ('building_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gatherer.Building')),
            ],
        ),
        migrations.CreateModel(
            name='List_Of_All_Appliance_in_building',
            fields=[
                ('appliance_type_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('appliance_name', models.CharField(max_length=45)),
                ('appliance_power', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pirate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('life', models.CharField(max_length=20)),
                ('years_active', models.CharField(max_length=20)),
                ('country_of_origin', models.CharField(max_length=20)),
                ('comments', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_id', models.CharField(max_length=45, unique=True)),
                ('room_name', models.CharField(max_length=45)),
                ('last_humidity', models.FloatField(null=True)),
                ('last_temperature', models.FloatField(null=True)),
                ('last_amount_CO2', models.FloatField(null=True)),
                ('last_reading_time', models.DateField()),
                ('nr_of_appliances', models.IntegerField()),
                ('flat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gatherer.Flat', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Room_Reading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reading_time', models.DateField(unique=True)),
                ('temperature', models.FloatField(null=True)),
                ('humidity', models.FloatField(null=True)),
                ('amount_of_CO2', models.FloatField(null=True)),
                ('flat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gatherer.Flat')),
                ('room_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gatherer.Room')),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('sensor_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('sensor_name', models.CharField(max_length=45)),
                ('sensor_function', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Sensor_Reading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('which_appliance', models.CharField(max_length=45)),
                ('sensor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gatherer.Sensor', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_id', models.IntegerField(unique=True)),
                ('unit_for', models.CharField(max_length=45)),
                ('unit', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('weather_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('reading_time', models.DateField()),
                ('temperature', models.FloatField(null=True)),
                ('humidity', models.FloatField(null=True)),
                ('windspeed', models.IntegerField()),
                ('wind_direction', models.IntegerField()),
                ('solar_rediation', models.FloatField(null=True)),
                ('amount_of_CO2', models.FloatField(null=True)),
                ('building_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gatherer.Building')),
            ],
        ),
        migrations.AddField(
            model_name='sensor_reading',
            name='unit_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gatherer.Unit', unique=True),
        ),
        migrations.AddField(
            model_name='appliance_reading',
            name='appliance_type_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gatherer.List_Of_All_Appliance_in_building'),
        ),
        migrations.AddField(
            model_name='appliance_reading',
            name='flat_id',
            field=models.ForeignKey(max_length=45, on_delete=django.db.models.deletion.CASCADE, to='gatherer.Flat'),
        ),
        migrations.AddField(
            model_name='appliance_reading',
            name='room_id',
            field=models.ForeignKey(max_length=45, on_delete=django.db.models.deletion.CASCADE, to='gatherer.Room'),
        ),
        migrations.AddField(
            model_name='appliance',
            name='appliance_type_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gatherer.List_Of_All_Appliance_in_building', unique=True),
        ),
        migrations.AddField(
            model_name='appliance',
            name='flat_id',
            field=models.ForeignKey(max_length=45, on_delete=django.db.models.deletion.CASCADE, to='gatherer.Flat', unique=True),
        ),
        migrations.AddField(
            model_name='appliance',
            name='room_id',
            field=models.ForeignKey(max_length=45, on_delete=django.db.models.deletion.CASCADE, to='gatherer.Room', unique=True),
        ),
    ]
