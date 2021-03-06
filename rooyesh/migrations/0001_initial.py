# Generated by Django 2.1 on 2019-02-19 10:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.TextField()),
                ('is_answer', models.BooleanField()),
                ('comment', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=12)),
                ('national_code', models.CharField(max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField(default=0)),
                ('choice', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rooyesh.Choice')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooyesh.Question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Week',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week_name', models.CharField(max_length=20)),
                ('expired', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='WeeklyAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week1', models.FloatField(default=0)),
                ('week2', models.FloatField(default=0)),
                ('week3', models.FloatField(default=0)),
                ('week4', models.FloatField(default=0)),
                ('week5', models.FloatField(default=0)),
                ('week6', models.FloatField(default=0)),
                ('week7', models.FloatField(default=0)),
                ('all_weeks', models.FloatField(default=0)),
                ('student_code', models.CharField(default=0, max_length=15)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='useranswer',
            name='week',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooyesh.Week'),
        ),
        migrations.AddField(
            model_name='question',
            name='week',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooyesh.Week'),
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooyesh.Question'),
        ),
        migrations.AddField(
            model_name='choice',
            name='week',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooyesh.Week'),
        ),
    ]
