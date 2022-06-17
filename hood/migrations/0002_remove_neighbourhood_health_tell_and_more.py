# Generated by Django 4.0.5 on 2022-06-17 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='neighbourhood',
            name='health_tell',
        ),
        migrations.RemoveField(
            model_name='neighbourhood',
            name='police_number',
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, null=True)),
                ('post', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('hood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hood_post', to='hood.neighbourhood')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_owner', to='hood.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('description', models.TextField(blank=True)),
                ('neighbourhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='business', to='hood.neighbourhood')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='hood.profile')),
            ],
        ),
    ]