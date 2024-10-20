# Generated by Django 5.1.2 on 2024-10-20 14:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cadastros', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='cidade',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ordemdecompra',
            name='cidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.cidade'),
        ),
        migrations.AddField(
            model_name='ordemdecompra',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='itemordemdecompra',
            name='ordem_de_compra',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastros.ordemdecompra'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='cidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.cidade'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='prefeitura',
            name='cidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.cidade'),
        ),
        migrations.AddField(
            model_name='prefeitura',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ordemdecompra',
            name='prefeitura',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.prefeitura'),
        ),
        migrations.AddField(
            model_name='produto',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='itemordemdecompra',
            name='produto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastros.produto'),
        ),
    ]