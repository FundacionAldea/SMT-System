# Generated by Django 4.0.5 on 2022-07-11 22:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('capacitaciones', '0006_alter_capacitaciones_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='capacitaciones',
            unique_together={('id_curren_user', 'conc_cap')},
        ),
    ]
