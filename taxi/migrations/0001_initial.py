<<<<<<< HEAD
# Generated by Django 4.2.3 on 2023-08-22 14:40
=======
# Generated by Django 4.2.3 on 2023-08-21 04:41
>>>>>>> ac0821965a66c3b8df718bcab8cbd71d7814e144

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
<<<<<<< HEAD
                ('phonenumber', models.CharField(max_length=1000)),
                ('Credit', models.FloatField()),
=======
                ('phone_number', models.CharField(max_length=15)),
                ('credit', models.FloatField()),
>>>>>>> ac0821965a66c3b8df718bcab8cbd71d7814e144
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
