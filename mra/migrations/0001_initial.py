# Generated by Django 2.2.4 on 2019-09-15 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MRA_List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('code', models.CharField(max_length=20)),
                ('market', models.CharField(choices=[('KOSPI', 'KOSPI'), ('KOSDAQ', 'KOSDAQ'), ('NASDAQ', 'NASDAQ')], default='KOSPI', max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('adf', models.DecimalField(decimal_places=3, max_digits=20, null=True)),
                ('adf_pv', models.DecimalField(decimal_places=3, max_digits=20, null=True)),
                ('adf_one', models.DecimalField(decimal_places=3, max_digits=20, null=True)),
                ('adf_five', models.DecimalField(decimal_places=3, max_digits=20, null=True)),
                ('hurst', models.DecimalField(decimal_places=3, max_digits=20, null=True)),
                ('half_life', models.DecimalField(decimal_places=3, max_digits=20, null=True)),
                ('sd', models.DecimalField(decimal_places=3, max_digits=20, null=True)),
                ('mean', models.DecimalField(decimal_places=3, max_digits=20, null=True)),
                ('volume', models.DecimalField(decimal_places=3, max_digits=20, null=True)),
                ('quantile_q1', models.IntegerField(null=True)),
                ('quantile_q2', models.IntegerField(null=True)),
                ('quantile_q3', models.IntegerField(null=True)),
                ('quantile_path', models.CharField(max_length=100, null=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]