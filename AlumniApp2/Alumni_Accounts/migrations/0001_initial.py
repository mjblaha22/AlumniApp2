# Generated by Django 3.1.1 on 2020-09-23 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Businesses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=200)),
                ('street_address', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=2)),
                ('zipcode', models.TextField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_place', models.CharField(max_length=200)),
                ('event_discription', models.CharField(max_length=200)),
                ('date_start', models.CharField(max_length=200)),
                ('time_start', models.CharField(max_length=200)),
                ('street_address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=2)),
                ('zipcode', models.TextField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=200)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('cohort', models.CharField(max_length=200)),
                ('business_name', models.CharField(max_length=200)),
                ('street_address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=2)),
                ('zipcode', models.CharField(max_length=6)),
                ('profile_image', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='User_Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='businessuser', to='Alumni_Accounts.businesses')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userbusiness', to='Alumni_Accounts.users')),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(max_length=1000)),
                ('business_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='busireview', to='Alumni_Accounts.businesses')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userreview', to='Alumni_Accounts.users')),
            ],
        ),
        migrations.CreateModel(
            name='Responses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response', models.CharField(max_length=1000)),
                ('message_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='messageresponse', to='Alumni_Accounts.messages')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userresponse', to='Alumni_Accounts.users')),
            ],
        ),
        migrations.AddField(
            model_name='messages',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='Alumni_Accounts.users'),
        ),
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='locations', to='Alumni_Accounts.businesses')),
                ('event_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='eventlocations', to='Alumni_Accounts.events')),
            ],
        ),
        migrations.AddField(
            model_name='events',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='events', to='Alumni_Accounts.users'),
        ),
        migrations.CreateModel(
            name='Emails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emails', to='Alumni_Accounts.users')),
            ],
        ),
        migrations.AddField(
            model_name='businesses',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='businesses', to='Alumni_Accounts.users'),
        ),
    ]
