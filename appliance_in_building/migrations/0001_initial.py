# Generated by Django 2.0 on 2018-04-10 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='List_Of_All_Appliance_in_building',
            fields=[
                ('appliance_type_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('appliance_name', models.CharField(max_length=45)),
                ('appliance_power', models.IntegerField()),
            ],
        ),
    ]
