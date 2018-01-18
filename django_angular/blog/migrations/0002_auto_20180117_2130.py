# Generated by Django 2.0 on 2018-01-18 02:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('tagline', models.CharField(max_length=256)),
            ],
        ),
        migrations.AlterModelOptions(
            name='blogentry',
            options={'verbose_name': 'Blog entry', 'verbose_name_plural': 'Blog entries'},
        ),
        migrations.AlterField(
            model_name='blogentry',
            name='text',
            field=models.TextField(verbose_name='blog entry text'),
        ),
        migrations.AddField(
            model_name='blogentry',
            name='blog',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='blog.Blog'),
            preserve_default=False,
        ),
    ]
