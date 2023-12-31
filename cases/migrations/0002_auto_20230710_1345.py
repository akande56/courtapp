# Generated by Django 3.2.12 on 2023-07-10 13:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cases', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='evidence',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected'), ('Under Review', 'Under Review')], default='Pending', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hearing',
            name='presiding_judge',
            field=models.ForeignKey(default=4, limit_choices_to={'is_judge': True}, on_delete=django.db.models.deletion.CASCADE, related_name='presiding_judge_hearings', to='users.user'),
            preserve_default=False,
        ),
    ]
