# Generated by Django 3.1.7 on 2022-02-23 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0005_contactformsubmission'),
    ]

    operations = [
        migrations.CreateModel(
            name='CareersPage',
            fields=[
                ('tworockpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cms.tworockpage')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.tworockpage',),
        ),
    ]