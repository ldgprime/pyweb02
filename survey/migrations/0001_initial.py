# Generated by Django 3.0.4 on 2020-03-27 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('answer_idx', models.AutoField(primary_key=True, serialize=False)),
                ('survey_idx', models.IntegerField()),
                ('num', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('survey_idx', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.TextField()),
                ('ans1', models.TextField(null=True)),
                ('ans2', models.TextField(null=True)),
                ('ans3', models.TextField(null=True)),
                ('ans4', models.TextField(null=True)),
                ('status', models.CharField(default='y', max_length=1)),
            ],
        ),
    ]
