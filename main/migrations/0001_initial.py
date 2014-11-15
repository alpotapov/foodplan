# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('water_g', models.DecimalField(max_digits=10, decimal_places=5)),
                ('energy_kcal', models.DecimalField(max_digits=10, decimal_places=5)),
                ('protein_g', models.DecimalField(max_digits=10, decimal_places=5)),
                ('lipid_total_g', models.DecimalField(max_digits=10, decimal_places=5)),
                ('ash_g', models.DecimalField(max_digits=10, decimal_places=5)),
                ('carbohydrt_g', models.DecimalField(max_digits=10, decimal_places=5)),
                ('fiber_td_g', models.DecimalField(max_digits=10, decimal_places=5)),
                ('sugar_tot_g', models.DecimalField(max_digits=10, decimal_places=5)),
                ('calcium_mg', models.DecimalField(max_digits=10, decimal_places=5)),
                ('iron_mg', models.DecimalField(max_digits=10, decimal_places=5)),
                ('magnesium_mg', models.DecimalField(max_digits=10, decimal_places=5)),
                ('phosphorus_mg', models.DecimalField(max_digits=10, decimal_places=5)),
                ('potassium_mg', models.DecimalField(max_digits=10, decimal_places=5)),
                ('sodium_mg', models.DecimalField(max_digits=10, decimal_places=5)),
                ('zinc_mg', models.DecimalField(max_digits=10, decimal_places=5)),
                ('copper_mg', models.DecimalField(max_digits=10, decimal_places=5)),
                ('manganese_mg', models.DecimalField(max_digits=10, decimal_places=5)),
                ('selenium_mig', models.DecimalField(max_digits=10, decimal_places=5)),
                ('vit_c_mg', models.DecimalField(max_digits=10, decimal_places=5)),
                ('thiamin_mg', models.DecimalField(max_digits=10, decimal_places=5)),
                ('riboflavin_mg', models.DecimalField(max_digits=10, decimal_places=5)),
                ('niacin_mg', models.DecimalField(max_digits=10, decimal_places=5)),
                ('panto_acid_mg', models.DecimalField(max_digits=10, decimal_places=5)),
                ('vit_b6_mg', models.DecimalField(max_digits=10, decimal_places=5)),
                ('folate_tot_mig', models.DecimalField(max_digits=10, decimal_places=5)),
                ('folic_acid_mig', models.DecimalField(max_digits=10, decimal_places=5)),
                ('food_folate_mig', models.DecimalField(max_digits=10, decimal_places=5)),
                ('folate_dfe_mig', models.DecimalField(max_digits=10, decimal_places=5)),
                ('choline_tot_mg', models.DecimalField(max_digits=10, decimal_places=5)),
                ('vit_b12_mig', models.DecimalField(max_digits=10, decimal_places=5)),
                ('vit_a_iu', models.DecimalField(max_digits=10, decimal_places=5)),
                ('vit_a_rae', models.DecimalField(max_digits=10, decimal_places=5)),
                ('retinol_mig', models.DecimalField(max_digits=10, decimal_places=5)),
                ('alpha_carot_mig', models.DecimalField(max_digits=10, decimal_places=5)),
                ('beta_carot_mig', models.DecimalField(max_digits=10, decimal_places=5)),
                ('beta_crypt_mig', models.DecimalField(max_digits=10, decimal_places=5)),
                ('lycopene_mig', models.DecimalField(max_digits=10, decimal_places=5)),
                ('lut_zea_mig', models.DecimalField(max_digits=10, decimal_places=5)),
                ('vit_e_mg', models.DecimalField(max_digits=10, decimal_places=5)),
                ('vit_d_mig', models.DecimalField(max_digits=10, decimal_places=5)),
                ('vit_d_iu', models.DecimalField(max_digits=10, decimal_places=5)),
                ('vit_k_mig', models.DecimalField(max_digits=10, decimal_places=5)),
                ('fa_sat_g', models.DecimalField(max_digits=10, decimal_places=5)),
                ('fa_mono_g', models.DecimalField(max_digits=10, decimal_places=5)),
                ('fa_poly_g', models.DecimalField(max_digits=10, decimal_places=5)),
                ('cholestrl_mg', models.DecimalField(max_digits=10, decimal_places=5)),
                ('gmwt_1', models.DecimalField(max_digits=10, decimal_places=5)),
                ('gmwt_desc1', models.CharField(max_length=255)),
                ('gmwt_2', models.DecimalField(max_digits=10, decimal_places=5)),
                ('gmwt_desc2', models.CharField(max_length=255)),
                ('refuse_pct', models.DecimalField(max_digits=10, decimal_places=5)),
                ('foodgroup', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('image_url', models.CharField(max_length=255)),
                ('prep_time_seconds', models.IntegerField(default=1200)),
                ('steps_json', models.TextField(default=b'')),
                ('ingredients_json', models.TextField(default=b'')),
                ('recipe_json', models.TextField(default=b'')),
                ('detailed_json', models.TextField(default=b'')),
                ('servings', models.IntegerField(default=1)),
                ('price', models.DecimalField(default=5.0, max_digits=10, decimal_places=2)),
                ('is_vegetarian', models.BooleanField(default=True)),
                ('is_lactose_intolerant', models.BooleanField(default=True)),
                ('is_breakfast', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ScheduledMeal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('recipe_id', models.IntegerField(default=0)),
                ('date', models.DateField(default=datetime.date.today)),
                ('user_id', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_vegetarian', models.BooleanField(default=False)),
                ('gender', models.IntegerField(default=0)),
                ('mouths', models.IntegerField(default=1)),
                ('age', models.IntegerField(default=20)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserIngredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ingredient_id', models.IntegerField(default=1001)),
                ('user_id', models.ForeignKey(to='main.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
