# Generated by Django 3.0.6 on 2020-05-29 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200529_0117'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30)),
                ('email', models.CharField(blank=True, max_length=50)),
                ('subject', models.CharField(blank=True, max_length=50)),
                ('message', models.TextField(blank=True, max_length=500)),
                ('status', models.CharField(choices=[('New', 'New'), ('Read', 'Read'), ('Closed', 'Closed')], default='New', max_length=10)),
                ('ip', models.CharField(blank=True, max_length=30)),
                ('note', models.CharField(blank=True, max_length=100)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
