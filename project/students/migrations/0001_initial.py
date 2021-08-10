# Generated by Django 2.1.7 on 2021-08-08 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('standard', models.CharField(max_length=20)),
                ('section', models.CharField(max_length=2)),
                ('session', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='score',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scores', to='students.Student'),
        ),
        migrations.AddField(
            model_name='score',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.Subject'),
        ),
        migrations.AlterUniqueTogether(
            name='score',
            unique_together={('student', 'subject')},
        ),
    ]