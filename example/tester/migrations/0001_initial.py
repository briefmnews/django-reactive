# Generated by Django 2.0.9 on 2018-12-08 12:25

from django.db import migrations, models
import django_reactive.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('simple', django_reactive.fields.ReactJSONSchemaField(default=dict, help_text='Simple')),
                ('nested', django_reactive.fields.ReactJSONSchemaField(default=dict, help_text='Nested')),
                ('arrays', django_reactive.fields.ReactJSONSchemaField(default=dict, help_text='Arrays')),
                ('numbers', django_reactive.fields.ReactJSONSchemaField(default=dict, help_text='Numbers')),
                ('widgets', django_reactive.fields.ReactJSONSchemaField(default=dict, help_text='Widgets')),
                ('ordering', django_reactive.fields.ReactJSONSchemaField(default=dict, help_text='Ordering')),
                ('references', django_reactive.fields.ReactJSONSchemaField(default=dict)),
                ('errors', django_reactive.fields.ReactJSONSchemaField(default=dict, help_text='Errors')),
                ('large', django_reactive.fields.ReactJSONSchemaField(default=dict, help_text='Large')),
                ('date_and_time', django_reactive.fields.ReactJSONSchemaField(default=dict, help_text='Date and time')),
                ('validation', django_reactive.fields.ReactJSONSchemaField(default=dict, help_text='Validation')),
                ('file', django_reactive.fields.ReactJSONSchemaField(default=dict, help_text='Files')),
                ('alternatives', django_reactive.fields.ReactJSONSchemaField(default=dict, help_text='Alternatives')),
                ('property_dependencies', django_reactive.fields.ReactJSONSchemaField(default=dict, help_text='Property dependencies')),
                ('schema_dependencies', django_reactive.fields.ReactJSONSchemaField(default=dict, help_text='Schema dependencies')),
            ],
        ),
    ]
