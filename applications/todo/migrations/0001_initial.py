# Generated by Django 2.1.1 on 2018-09-27 13:43

import applications.todo.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=1000, null=True)),
                ('due_datetime', models.DateTimeField()),
                ('status', models.CharField(choices=[(applications.todo.models.TaskStatus('pending'), 'pending'), (applications.todo.models.TaskStatus('in_progress'), 'in_progress'), (applications.todo.models.TaskStatus('done'), 'done')], max_length=5)),
                ('list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.List')),
            ],
        ),
    ]
