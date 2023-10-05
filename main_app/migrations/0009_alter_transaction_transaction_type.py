# Generated by Django 4.2.3 on 2023-10-05 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_alter_creditcard_card_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.CharField(choices=[('Transfer', 'Transfer'), ('Received', 'Received'), ('Withdraw', 'Withdraw'), ('Refund', 'Refund'), ('Request', 'Payment Request'), ('Deposit', 'Deposit'), ('None', 'None')], default='None', max_length=100),
        ),
    ]
