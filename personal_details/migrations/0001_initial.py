# Generated by Django 2.0 on 2018-04-10 10:50

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('flat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Personal_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('birthdate', models.DateField()),
                ('food_preference', models.CharField(max_length=45)),
                ('last_sleep_from', models.DateTimeField()),
                ('last_sleep_till', models.DateTimeField()),
                ('first_name', models.CharField(max_length=45)),
                ('middle_name', models.CharField(max_length=45, null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('age', models.IntegerField()),
                ('email', models.CharField(max_length=45, null=True)),
                ('phone_nr', models.CharField(max_length=45, null=True)),
                ('flat_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='flat.Flat')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
    ]