# Generated by Django 4.1.2 on 2022-12-12 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AsesoriaTecnica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tecnico', models.CharField(max_length=255, verbose_name='tecnico')),
                ('id_curren_user', models.IntegerField(default=0)),
                ('conc_asesoria', models.IntegerField()),
                ('programa', models.CharField(max_length=255, verbose_name='programa')),
                ('proyecto', models.CharField(max_length=255, verbose_name='proyecto')),
                ('fecha', models.DateField(verbose_name='fecha_asesoria')),
                ('hora', models.TimeField(verbose_name='hora_asesoria')),
                ('nombre_finca', models.CharField(max_length=255, verbose_name='nombre_finca')),
                ('etapa_fenologica', models.CharField(max_length=255, verbose_name='etapa_fenologica')),
            ],
            options={
                'unique_together': {('id_curren_user', 'conc_asesoria', 'fecha')},
            },
        ),
        migrations.CreateModel(
            name='recomendaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recomendacion', models.CharField(max_length=255, verbose_name='recomendacion')),
                ('id_rel_asesoria', models.IntegerField(default=0)),
                ('asesoria_recomendacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asesoria_recomendacion', to='asesoria.asesoriatecnica', verbose_name='asesoria_recomendacion')),
            ],
        ),
        migrations.CreateModel(
            name='Plagas_enfermedades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manejo_sombra', models.IntegerField(verbose_name='manejo_sombra')),
                ('manejo_maleza', models.IntegerField(verbose_name='manejo_maleza')),
                ('incidencia_broca', models.IntegerField(verbose_name='incidencia_broca')),
                ('actracnosis', models.IntegerField(verbose_name='actracnosis')),
                ('ojo_gallo', models.IntegerField(verbose_name='ojo_gallo')),
                ('roya', models.IntegerField(verbose_name='roya')),
                ('pellejillo', models.IntegerField(verbose_name='pellejillo')),
                ('mancha_hierro', models.IntegerField(verbose_name='mancha_hierro')),
                ('cochinilla', models.IntegerField(default=0, verbose_name='cochinilla')),
                ('minador', models.IntegerField(default=0, verbose_name='minador')),
                ('picudo', models.IntegerField(default=0, verbose_name='picudo')),
                ('derrite', models.IntegerField(default=0, verbose_name='derrite')),
                ('bacteriosis', models.IntegerField(verbose_name='bacteriosis')),
                ('id_rel_asesoria', models.IntegerField(default=0)),
                ('asesoria_enfermedades_plagas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asesoria_enfermedades_plagas', to='asesoria.asesoriatecnica', verbose_name='asesoria_enfermedades_plagas')),
            ],
        ),
        migrations.CreateModel(
            name='Fertalizacion_foliar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fertilizacion_foliar', models.CharField(max_length=255, verbose_name='fertilizacion_foliar')),
                ('estadoAPlantacionFoliar', models.CharField(default=0, max_length=255, verbose_name='estadoAPlantacionFoliar')),
                ('producto_foliar', models.CharField(max_length=255, verbose_name='producto_foliar')),
                ('medidaProdFoliar', models.CharField(default=0, max_length=255, verbose_name='medidaProdFoliar')),
                ('dosis_foliar', models.FloatField(verbose_name='dosis_foliar')),
                ('id_rel_asesoria', models.IntegerField(default=0)),
                ('asesoria_foliar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asesoria_foliar', to='asesoria.asesoriatecnica', verbose_name='asesoria_foliar')),
            ],
        ),
        migrations.CreateModel(
            name='Fertalizacion_edafica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fertilizacion_edafica', models.CharField(max_length=255, verbose_name='fertilizacion_edafica')),
                ('producto_edafico', models.CharField(max_length=255, verbose_name='producto_edafico')),
                ('estadoAPlantacionFe', models.CharField(default=0, max_length=255, verbose_name='estadoAPlantacionFe')),
                ('dosis_edafica', models.FloatField(verbose_name='dosis_edafica')),
                ('id_rel_asesoria', models.IntegerField(default=0)),
                ('asesoria_edafica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asesoria_edafica', to='asesoria.asesoriatecnica', verbose_name='asesoria_edafica')),
            ],
        ),
        migrations.CreateModel(
            name='entradas_salidas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_curren_user', models.IntegerField()),
                ('conce_entrada_salida', models.IntegerField()),
                ('codAsociado', models.IntegerField(default=0)),
                ('momentoMarca', models.CharField(default='Pendiente', max_length=100)),
                ('longitud', models.FloatField(default=0.0, verbose_name='longitud')),
                ('latitud', models.FloatField(default=0.0, verbose_name='latitud')),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
            ],
            options={
                'unique_together': {('id_curren_user', 'conce_entrada_salida', 'fecha')},
            },
        ),
        migrations.CreateModel(
            name='Enmienda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fertilizacion', models.CharField(max_length=255, verbose_name='fertilizacion_foliar')),
                ('producto_enmienda', models.CharField(max_length=255, verbose_name='producto_enmienda')),
                ('estadoAPlantacionEnmienda', models.CharField(default=0, max_length=255, verbose_name='estadoAPlantacionEnmienda')),
                ('dosis_enmienda', models.FloatField(verbose_name='dosis_enmienda')),
                ('medidaEnmienda', models.CharField(default='Empty', max_length=100, verbose_name='medidaEnmienda')),
                ('id_rel_asesoria', models.IntegerField(default=0)),
                ('asesoria_enmienda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asesoria_enmienda', to='asesoria.asesoriatecnica', verbose_name='asesoria_enmienda')),
            ],
        ),
        migrations.CreateModel(
            name='AsociadoAsesoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod', models.IntegerField(verbose_name='cod')),
                ('nombres_apellidos', models.CharField(max_length=255, verbose_name='nombres_y_apellidos')),
                ('cedula', models.CharField(max_length=255, verbose_name='cedula')),
                ('edad', models.IntegerField()),
                ('sexo', models.CharField(default='1', max_length=15, verbose_name='sexo')),
                ('departamento', models.CharField(default='Jinotega', max_length=255, verbose_name='departamento')),
                ('municipio', models.CharField(default='Jinotega', max_length=100, verbose_name='departamento')),
                ('comunidad', models.CharField(default='Jinotega', max_length=100, verbose_name='comunidad')),
                ('rubro', models.CharField(blank=True, default='otro', max_length=255, null=True, verbose_name='rubro')),
                ('manzanas_suelo', models.FloatField(default=0)),
                ('latitud', models.FloatField(default=0.0, verbose_name='latitud')),
                ('longitud', models.FloatField(default=0.0, verbose_name='longitud')),
                ('estado', models.CharField(default='', max_length=255, verbose_name='estado')),
                ('fecha_asociacion', models.CharField(default='', max_length=255, verbose_name='fecha_asociacion')),
                ('id_rel_asesoria', models.IntegerField(default=0, verbose_name='id_rel_asesoria')),
                ('asesoria_socio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asesoria_socio', to='asesoria.asesoriatecnica', verbose_name='asesoria_socio')),
            ],
            options={
                'ordering': ['cod'],
            },
        ),
        migrations.CreateModel(
            name='Asesoriadetalles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_total_finca', models.FloatField(verbose_name='area_total_finca')),
                ('area_total_cafe', models.FloatField(verbose_name='area_total_cafe')),
                ('area_cafe_desarrollo', models.FloatField(verbose_name='area_cafe_desarrollo')),
                ('area_cafe_productivo', models.FloatField(verbose_name='area_cafe_productivo')),
                ('manejo_podas', models.FloatField(verbose_name='manejo_podas')),
                ('diagnostico', models.BooleanField(verbose_name='diagnostico')),
                ('analisis_suelo', models.BooleanField(verbose_name='analisis_suelo')),
                ('plan_manejo', models.BooleanField(verbose_name='plan_manejo')),
                ('auditoria_interna', models.BooleanField(verbose_name='auditoria_interna')),
                ('estimada_cosecha', models.BooleanField(verbose_name='estimada_cosecha')),
                ('acceso_credito', models.BooleanField(verbose_name='acceso_credito')),
                ('motivo_no_credito', models.CharField(max_length=255, verbose_name='motivo_no_credito')),
                ('id_rel_asesoria', models.IntegerField(default=0, verbose_name='id_rel_asesoria')),
                ('asesoria_detalle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asesoria_detalle', to='asesoria.asesoriatecnica', verbose_name='asesoria_detalle')),
            ],
        ),
    ]
