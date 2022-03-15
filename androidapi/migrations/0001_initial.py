# Generated by Django 3.2.4 on 2022-02-11 09:43

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('status', models.IntegerField()),
                ('created_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'college',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Adminlogins',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('email_verified_at', models.DateTimeField(blank=True, null=True)),
                ('mobile', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=500, null=True)),
                ('registration_id', models.CharField(blank=True, max_length=500, null=True)),
                ('user_image', models.CharField(blank=True, max_length=500, null=True)),
                ('user_status', models.CharField(max_length=5)),
                ('password', models.CharField(max_length=255)),
                ('remember_token', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'adminlogins',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ApplyEmpInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_created=True, blank=True, default=None)),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('phoneno', models.CharField(max_length=11)),
                ('fullsizephoto', models.CharField(default=None, max_length=250)),
                ('whphoneno', models.CharField(max_length=11)),
                ('email', models.CharField(max_length=200)),
                ('password', models.TextField()),
                ('profile_status', models.IntegerField()),
                ('Aadhar_front_img', models.CharField(blank=True, max_length=200, null=True)),
                ('Aadhar_back_img', models.CharField(blank=True, max_length=200, null=True)),
                ('paddress', models.TextField(blank=True, null=True)),
                ('caddress', models.TextField(blank=True, null=True)),
                ('branch', models.IntegerField(blank=True, null=True)),
                ('photo', models.CharField(max_length=250)),
                ('resume', models.CharField(max_length=250, null=True)),
                ('longitude', models.CharField(max_length=100)),
                ('lattitude', models.CharField(max_length=100)),
                ('gender', models.IntegerField()),
                ('status', models.IntegerField(default=1, null=True)),
                ('canhirestatus', models.IntegerField(default=0, null=True)),
                ('regid', models.CharField(default=None, max_length=40, null=True)),
                ('state_id', models.IntegerField(default=None, null=True)),
                ('dist_id', models.IntegerField(default=None, null=True)),
                ('loginpin', models.CharField(default=None, max_length=5, null=True)),
                ('referal_code', models.CharField(default=None, max_length=50, null=True)),
                ('device_token', models.CharField(default=None, max_length=250, null=True)),
                ('college', models.ForeignKey(db_column='college', on_delete=django.db.models.deletion.CASCADE, to='androidapi.college')),
            ],
            options={
                'db_table': 'apply_emp_info',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Appversion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(max_length=20)),
                ('link', models.TextField()),
                ('type', models.IntegerField()),
                ('changes', models.TextField()),
                ('created_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'appversion',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'board',
            },
        ),
        migrations.CreateModel(
            name='Contactus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=250)),
                ('phoneno', models.CharField(max_length=10)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'contactus',
            },
        ),
        migrations.CreateModel(
            name='Job_profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('status', models.IntegerField()),
                ('type', models.IntegerField()),
                ('sub_type', models.IntegerField()),
                ('hiretype', models.IntegerField()),
            ],
            options={
                'db_table': 'job_profile',
            },
        ),
        migrations.CreateModel(
            name='JobCode',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=20)),
                ('valid_date', models.DateTimeField(blank=True, null=True)),
                ('code_type', models.IntegerField(default=1)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'JobCode',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PassingYear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('name', models.IntegerField()),
            ],
            options={
                'db_table': 'passing_year',
            },
        ),
        migrations.CreateModel(
            name='Stream_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_created=True)),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('name', models.TextField()),
                ('status', models.IntegerField()),
            ],
            options={
                'db_table': 'stream_type',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TIPActivationCode',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=20)),
                ('valid_date', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'tipactivation_code',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Voucher_Code',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_created=True)),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('code', models.TextField()),
                ('price', models.TextField()),
                ('status', models.IntegerField()),
            ],
            options={
                'db_table': 'voucher_code',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Tippayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=10)),
                ('transactionid', models.CharField(default=None, max_length=100, null=True)),
                ('payment_date', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('emp', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='androidapi.applyempinfo')),
            ],
            options={
                'db_table': 'tippayment',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TipCampusexecutive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('emp', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='androidapi.applyempinfo')),
            ],
            options={
                'db_table': 'TipCampusexecutive',
            },
        ),
        migrations.CreateModel(
            name='HrTarget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True, default=django.utils.timezone.now)),
                ('target', models.CharField(max_length=5)),
                ('month', models.IntegerField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('emp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='androidapi.applyempinfo')),
            ],
            options={
                'db_table': 'hrtarget',
            },
        ),
        migrations.CreateModel(
            name='EmpReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True, default=django.utils.timezone.now)),
                ('workingstatus', models.IntegerField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('emp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='androidapi.applyempinfo')),
            ],
            options={
                'db_table': 'empreport',
            },
        ),
        migrations.CreateModel(
            name='EmpkeySkill',
            fields=[
                ('created_at', models.DateTimeField()),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('emp', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='androidapi.applyempinfo')),
            ],
            options={
                'db_table': 'empkeyskill',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='EmpEducations',
            fields=[
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('hq_type', models.IntegerField()),
                ('school_medium', models.IntegerField(blank=True, null=True)),
                ('total_marks', models.CharField(blank=True, max_length=5, null=True)),
                ('board', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='androidapi.board')),
                ('emp', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='androidapi.applyempinfo')),
                ('py', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='androidapi.passingyear')),
            ],
            options={
                'db_table': 'emp_educations',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='applyempinfo',
            name='course_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='androidapi.stream_type'),
        ),
        migrations.AddField(
            model_name='applyempinfo',
            name='passing_year',
            field=models.ForeignKey(db_column='passing_year', on_delete=django.db.models.deletion.CASCADE, to='androidapi.passingyear'),
        ),
        migrations.AddField(
            model_name='applyempinfo',
            name='selected_job_profile',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='androidapi.job_profile'),
        ),
        migrations.CreateModel(
            name='Applied',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('apply_type', models.IntegerField()),
                ('type', models.IntegerField()),
                ('status', models.IntegerField(null=True)),
                ('interview_date', models.DateTimeField(null=True)),
                ('contactname', models.CharField(default=None, max_length=100, null=True)),
                ('contactno', models.CharField(default=None, max_length=10, null=True)),
                ('location', models.CharField(default=None, max_length=50, null=True)),
                ('address', models.TextField(default=None, null=True)),
                ('instruction', models.TextField(default=None, null=True)),
                ('Transactionid', models.CharField(default=None, max_length=100, null=True)),
                ('amount_to_paid', models.CharField(default=None, max_length=50, null=True)),
                ('amount_paid', models.CharField(default=None, max_length=50, null=True)),
                ('voucher_code', models.CharField(default=None, max_length=100, null=True)),
                ('enroll_expire_date', models.DateTimeField(default=None, null=True)),
                ('payment_date', models.DateTimeField(default=None, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('emp', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='androidapi.applyempinfo')),
                ('jobcode', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='androidapi.jobcode')),
                ('jobprofile', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='androidapi.job_profile')),
            ],
            options={
                'db_table': 'applied',
                'managed': True,
            },
        ),
    ]
