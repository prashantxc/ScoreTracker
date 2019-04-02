# Generated by Django 2.1.2 on 2019-04-02 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PlayerOne', models.CharField(max_length=100)),
                ('PlayerTwo', models.CharField(max_length=100)),
                ('Score', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='match',
            unique_together={('PlayerOne', 'PlayerTwo')},
        ),
    ]