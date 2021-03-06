# Generated by Django 3.1.4 on 2021-02-21 15:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('first_name', models.CharField(max_length=255, verbose_name='name')),
                ('last_name', models.CharField(max_length=255, verbose_name='last name')),
                ('role', models.CharField(choices=[('user', 'user'), ('moderator', 'moderator'), ('admin', 'admin')], default='user', max_length=9, verbose_name='role')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('phone_number', models.CharField(max_length=20, unique=True)),
                ('time_to_call', models.CharField(max_length=3000, verbose_name='time to call')),
                ('status', models.CharField(choices=[('blocked', 'blocked'), ('active', 'active'), ('email verification', 'email verification')], default='active', max_length=20, verbose_name='status')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='title')),
                ('description', models.TextField(verbose_name='description')),
                ('publication_date', models.DateTimeField(auto_now_add=True, verbose_name='publication date')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='price')),
                ('views', models.IntegerField(default=0, editable=False, verbose_name='views')),
                ('photos', models.ImageField(upload_to='photos/', verbose_name='photos')),
                ('status', models.CharField(choices=[('draft', 'draft'), ('moderation', 'moderation'), ('rejected', 'rejected'), ('sales', 'sales'), ('active', 'active')], default='draft', max_length=20, verbose_name='status')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='uuid')),
                ('description', models.CharField(max_length=5000, verbose_name='description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='RegionDirectory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='CitiesDirectory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bulletin_board.regiondirectory', verbose_name='region')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='AdModerationRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moderation_date', models.DateTimeField(auto_now=True, verbose_name='moderation date')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bulletin_board.ad', verbose_name='ad')),
                ('moderator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='moderator')),
            ],
        ),
        migrations.AddField(
            model_name='ad',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bulletin_board.category', verbose_name='category'),
        ),
        migrations.AddField(
            model_name='ad',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bulletin_board.citiesdirectory', verbose_name='city'),
        ),
        migrations.AddField(
            model_name='ad',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='owner'),
        ),
    ]
