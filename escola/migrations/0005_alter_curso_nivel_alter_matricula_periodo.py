# Generated by Django 4.2.7 on 2023-11-19 06:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("escola", "0004_alter_curso_nivel_alter_matricula_periodo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="curso",
            name="nivel",
            field=models.CharField(
                choices=[("B", "Básico"), ("I", "Intermediário"), ("A", "Avançado")],
                default="B",
                max_length=1,
            ),
        ),
        migrations.AlterField(
            model_name="matricula",
            name="periodo",
            field=models.CharField(
                choices=[("M", "Manhã"), ("N", "Noite"), ("T", "Tarde")],
                default="M",
                max_length=1,
            ),
        ),
    ]
