# Generated by Django 5.0.3 on 2024-04-03 21:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Account",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "bank_name",
                    models.CharField(max_length=100, verbose_name="Bank Name"),
                ),
                (
                    "account_number",
                    models.CharField(
                        max_length=20, unique=True, verbose_name="Account Number"
                    ),
                ),
                (
                    "ifsc_code",
                    models.CharField(max_length=11, verbose_name="IFSC Code"),
                ),
                (
                    "balance",
                    models.DecimalField(
                        decimal_places=2, max_digits=14, verbose_name="Balance"
                    ),
                ),
            ],
            options={"verbose_name": "Account", "verbose_name_plural": "Accounts",},
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("category", models.CharField(max_length=100)),
                ("category_description", models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="UserData",
            fields=[
                (
                    "Name",
                    models.CharField(max_length=100, primary_key=True, serialize=False),
                ),
                ("Date_of_birth", models.DateField()),
                ("Profession", models.CharField(max_length=100)),
                ("Address", models.TextField()),
                ("Fixed_salary", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "Variable_salary",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                (
                    "In_hand_salary",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("CTC", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={"ordering": ["Name"],},
        ),
        migrations.CreateModel(
            name="Savings",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "emergency_fund",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                (
                    "retirement_savings",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                (
                    "education_savings",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                (
                    "medical_savings",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                (
                    "others",
                    models.DecimalField(decimal_places=2, max_digits=10, null=True),
                ),
                ("account", models.ManyToManyField(to="user_expense.account")),
                (
                    "user_data",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="user_expense.userdata",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Expenses",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Amount", models.DecimalField(decimal_places=2, max_digits=10)),
                ("description", models.CharField(max_length=100, null=True)),
                ("account", models.ManyToManyField(to="user_expense.account")),
                ("category", models.ManyToManyField(to="user_expense.category")),
                (
                    "user_data",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="user_expense.userdata",
                    ),
                ),
            ],
        ),
    ]
