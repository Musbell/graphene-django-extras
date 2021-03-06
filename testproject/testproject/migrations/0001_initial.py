# Generated by Django 2.0.2 on 2018-07-15 05:45

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('org_type', models.CharField(choices=[('partner', 'Partner'), ('facilitator', 'Facilitator'), ('consultant', 'Consultant'), ('supplier', 'Supplier')], max_length=20)),
                ('website', models.URLField(blank=True, verbose_name='Organization URL')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(default='TBD', max_length=255)),
                ('list_price', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('product_url', models.URLField(blank=True)),
                ('spec_reviewed_date', models.DateField(blank=True, null=True)),
                ('lead_time_days', models.IntegerField(blank=True, null=True)),
                ('is_discontinued', models.NullBooleanField(default=None)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ProductFeatureAttributes',
            fields=[
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='feature_attributes', serialize=False, to='testproject.Product')),
                ('seismic', models.BooleanField(default=False)),
                ('ada', models.BooleanField(default=False)),
                ('antimicrobial', models.BooleanField(default=False)),
                ('green', models.BooleanField(default=False)),
                ('opa', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'verbose_name_plural': 'product feature attributes',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='testproject.Category'),
        ),
        migrations.AddField(
            model_name='product',
            name='manufacturer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='manufactured_products', to='testproject.Organization'),
        ),
        migrations.AddField(
            model_name='product',
            name='replacement_product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='testproject.Product'),
        ),
    ]
