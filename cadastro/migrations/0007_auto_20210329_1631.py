# Generated by Django 3.0.13 on 2021-03-29 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0006_auto_20210325_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opcaovoto',
            name='votacao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.Votacao', verbose_name='Votação'),
        ),
    ]
