# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-28 14:13
from __future__ import unicode_literals

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
            name='Can',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('strength_member', models.TextField()),
                ('strength_manager', models.TextField()),
                ('weekness_member', models.TextField()),
                ('weekness_manager', models.TextField()),
                ('action', models.TextField()),
                ('evaluation', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Must',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thema', models.TextField()),
                ('content', models.TextField()),
                ('evaluation', models.TextField()),
                ('score_member', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MustMission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal', models.TextField()),
                ('process', models.TextField()),
                ('to_report', models.TextField()),
                ('criteria', models.TextField()),
                ('weight', models.IntegerField()),
                ('result', models.TextField()),
                ('score_member', models.IntegerField()),
                ('score_manager', models.IntegerField()),
                ('must', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wcm.Must')),
            ],
        ),
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('sort_no', models.IntegerField()),
                ('ins_at', models.DateTimeField(auto_now_add=True)),
                ('upd_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('first', '作成中'), ('second', '上長コメント中'), ('exe', '実践中'), ('eval', '振り返り'), ('end', '終了')], max_length=5)),
                ('ins_at', models.DateTimeField(auto_now_add=True)),
                ('upd_at', models.DateTimeField(auto_now=True)),
                ('period', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wcm.Period')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Will',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('realize_member', models.TextField()),
                ('realize_manager', models.TextField()),
                ('career_image_member', models.TextField()),
                ('career_image_manager', models.TextField()),
                ('sheet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wcm.Sheet')),
            ],
        ),
        migrations.AddField(
            model_name='must',
            name='sheet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wcm.Sheet'),
        ),
        migrations.AddField(
            model_name='can',
            name='sheet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wcm.Sheet'),
        ),
    ]
