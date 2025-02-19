# Generated by Django 4.2 on 2025-02-12 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authcart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderUpdate',
            fields=[
                ('update_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField(default='')),
                ('update_desc', models.CharField(max_length=5000)),
                ('delivered', models.BooleanField(default=False)),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
