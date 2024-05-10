# Generated by Django 5.0.4 on 2024-05-10 16:32

import django.db.models.deletion
import main.utilities
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rubric_subrubric_superrubric_rubric_super_rubric'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='Товар')),
                ('content', models.TextField(verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('contacts', models.TextField(verbose_name='Контакт')),
                ('image', models.ImageField(blank=True, upload_to='get_timestamp_path', verbose_name='Изображение')),
                ('is_active', models.BooleanField(db_index=True, default=True, verbose_name='Выводить в списке?')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор обьявление')),
                ('rubric', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.subrubric', verbose_name='Рубрика')),
            ],
            options={
                'verbose_name': 'Обьявление',
                'verbose_name_plural': 'Обьявления',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='AdditionalImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=main.utilities.get_timestamp_path, verbose_name='Изображение')),
                ('bb', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.bb', verbose_name='Обьявление')),
            ],
            options={
                'verbose_name': 'Дополнительная иллюстрация',
                'verbose_name_plural': 'Дополнительные иллюстрации',
            },
        ),
    ]