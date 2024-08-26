# Generated by Django 5.1 on 2024-08-24 11:15

import django.db.models.deletion
import phonenumber_field.modelfields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('age', models.IntegerField()),
                ('actor_image', models.ImageField(blank=True, null=True, upload_to='actors/')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('director_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('age', models.IntegerField()),
                ('director_image', models.ImageField(blank=True, null=True, upload_to='directors/')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('status', models.CharField(choices=[('Pro', 'Pro'), ('Simple', 'Simple')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=100)),
                ('movie_name_en', models.CharField(max_length=100, null=True)),
                ('movie_name_ru', models.CharField(max_length=100, null=True)),
                ('movie_name_ky', models.CharField(max_length=100, null=True)),
                ('date', models.DateField()),
                ('quality', models.CharField(choices=[('144', '144'), ('360', '360'), ('480', '480'), ('720', '720'), ('1080', '1080'), ('1080 Ultra', '1080 Ultra')], max_length=20)),
                ('movie_time', models.IntegerField()),
                ('description', models.TextField()),
                ('description_en', models.TextField(null=True)),
                ('description_ru', models.TextField(null=True)),
                ('description_ky', models.TextField(null=True)),
                ('movie_trailer', models.URLField(blank=True, null=True)),
                ('movie_image', models.ImageField(blank=True, null=True, upload_to='movies/')),
                ('status', models.CharField(choices=[('Pro', 'Pro'), ('Simple', 'Simple')], max_length=10)),
                ('actors', models.ManyToManyField(to='kino.actor')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kino.country')),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kino.director')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kino.genre')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='kino.comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kino.movie')),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='kino.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kino.movie')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')])),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kino.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cart', to='kino.userprofile'),
        ),
    ]
