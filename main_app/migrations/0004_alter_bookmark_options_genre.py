# Generated by Django 4.0.2 on 2022-02-12 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_bookmark_delete_log'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookmark',
            options={'ordering': ['-page']},
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name of Genre')),
                ('book', models.ManyToManyField(to='main_app.Book')),
            ],
        ),
    ]
