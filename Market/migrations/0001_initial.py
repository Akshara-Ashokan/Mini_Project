# Generated by Django 4.2 on 2023-04-19 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Guest', '0007_tbl_market_reg_mar_status'),
        ('Admin', '0011_rename_sad_eamil_tbl_subadmin_sad_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_market_product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdt_name', models.CharField(max_length=50)),
                ('pdt_rate', models.IntegerField()),
                ('pdt_dis', models.CharField(max_length=100)),
                ('pdt_stock', models.IntegerField()),
                ('pdt_image', models.FileField(upload_to='MarketProduct/')),
                ('market', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_market_reg')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_subcat')),
            ],
        ),
    ]
