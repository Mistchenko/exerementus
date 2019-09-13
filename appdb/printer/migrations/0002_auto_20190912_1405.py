# Generated by Django 2.2.5 on 2019-09-12 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('printer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='part',
            name='resource',
            field=models.PositiveIntegerField(default=0, help_text='На какое количество страниц рассчитан', verbose_name='Ресурс '),
        ),
        migrations.AlterField(
            model_name='printer',
            name='serial',
            field=models.CharField(db_index=True, default='', max_length=32, verbose_name='Серийный номер'),
        ),
    ]