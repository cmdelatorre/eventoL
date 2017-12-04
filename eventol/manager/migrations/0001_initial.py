# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-03 16:35
from __future__ import unicode_literals

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import image_cropping.fields
import manager.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('long_description', models.TextField(verbose_name='Long Description')),
                ('abstract', models.TextField(help_text='Short idea of the talk (Two or three sentences)', verbose_name='Abstract')),
                ('start_date', models.DateTimeField(blank=True, null=True, verbose_name='Start Time')),
                ('end_date', models.DateTimeField(blank=True, null=True, verbose_name='End Time')),
                ('type', models.CharField(blank=True, max_length=50, null=True, verbose_name='Type')),
                ('speakers_names', models.CharField(help_text="Comma separated speaker's names", max_length=600, verbose_name='Speakers Names')),
                ('speaker_contact', models.EmailField(help_text='Where can whe reach you from the organization team?', max_length=254, verbose_name='Speaker Contact')),
                ('labels', models.CharField(help_text='Comma separated tags. i.e. Linux, Free Software, Archlinux', max_length=200, verbose_name='Labels')),
                ('presentation', models.FileField(blank=True, help_text='Any material you are going to use for the talk (optional, but recommended)', null=True, upload_to='talks', verbose_name='Presentation')),
                ('level', models.CharField(choices=[('1', 'Beginner'), ('2', 'Medium'), ('3', 'Advanced')], help_text="Talk's Technical level", max_length=100, verbose_name='Level')),
                ('additional_info', models.TextField(blank=True, help_text='Any info you consider relevant for the organizer: i.e. Write here if your activity has any special requirement', null=True, verbose_name='Additional Info')),
                ('status', models.CharField(choices=[('1', 'Proposal'), ('2', 'Accepted'), ('3', 'Rejected')], help_text='Activity proposal status', max_length=20, verbose_name='Status')),
                ('image', image_cropping.fields.ImageCropField(blank=True, null=True, upload_to='images_thumbnails', verbose_name='Image')),
                ('cropping', image_cropping.fields.ImageRatioField('image', '700x450', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text='The image must be 700x450 px. You can crop it here.', hide_image_field=False, size_warning=True, verbose_name='Cropping')),
                ('is_dummy', models.BooleanField(default=False, help_text='A dummy activity is used for example for coffee breaks. We use this to exclude it from the index page and other places', verbose_name='Is a dummy Activity?')),
            ],
            options={
                'verbose_name': 'Activity',
                'ordering': ['title'],
                'verbose_name_plural': 'Activities',
            },
        ),
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Last Name')),
                ('nickname', models.CharField(blank=True, max_length=200, null=True, verbose_name='Nickname')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('is_installing', models.BooleanField(default=False, verbose_name='Is going to install?')),
                ('additional_info', models.CharField(blank=True, help_text='Any additional info you consider relevant for the organizers', max_length=200, null=True, verbose_name='Additional Info')),
                ('email_confirmed', models.BooleanField(default=False, verbose_name='Email confirmed?')),
                ('email_token', models.CharField(blank=True, max_length=200, null=True, verbose_name='Confirmation Token')),
                ('registration_date', models.DateTimeField(blank=True, null=True, verbose_name='Registration Date')),
            ],
            options={
                'verbose_name': 'Attendee',
                'verbose_name_plural': 'Attendees',
            },
        ),
        migrations.CreateModel(
            name='AttendeeAttendanceDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, help_text='The date of the attendance', verbose_name='Date')),
                ('attendee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.Attendee', verbose_name='Attendee')),
            ],
        ),
        migrations.CreateModel(
            name='Collaborator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignation', models.CharField(blank=True, help_text='Anything you can help with (i.e. Talks, Coffee...)', max_length=200, null=True, verbose_name='Assignation')),
                ('time_availability', models.CharField(blank=True, help_text='Time gap in which you can help during the event. i.e. "All the event", "Morning", "Afternoon", ...', max_length=200, null=True, verbose_name='Time Availability')),
                ('phone', models.CharField(blank=True, max_length=200, null=True, verbose_name='Phone')),
                ('address', models.CharField(blank=True, max_length=200, null=True, verbose_name='Address')),
                ('additional_info', models.CharField(blank=True, help_text='Any additional info you consider relevant', max_length=200, null=True, verbose_name='Additional Info')),
            ],
            options={
                'verbose_name': 'Collaborator',
                'verbose_name_plural': 'Collaborators',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(help_text='i.e. https://twitter.com/flisol', max_length=200, verbose_name='Direccion')),
                ('text', models.CharField(help_text='i.e. @Flisol', max_length=200, verbose_name='Text')),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
        ),
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('message', models.TextField(verbose_name='Message')),
            ],
            options={
                'verbose_name': 'Contact Message',
                'verbose_name_plural': 'Contact Messages',
            },
        ),
        migrations.CreateModel(
            name='ContactType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Name')),
                ('icon_class', models.CharField(max_length=200, verbose_name='Icon Class')),
                ('validate', models.CharField(choices=[('1', 'Validate URL'), ('2', 'Validate Email'), ('3', "Don't validate")], help_text='Type of field validation', max_length=10, verbose_name='Level')),
            ],
            options={
                'verbose_name': 'Contact Type',
                'verbose_name_plural': 'Contact Types',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Event Name')),
                ('limit_proposal_date', models.DateField(help_text='Limit date to submit talk proposals', verbose_name='Limit Proposals Date')),
                ('slug', models.CharField(help_text='For example: flisol-caba', max_length=200, unique=True, validators=[manager.models.validate_url], verbose_name='URL')),
                ('external_url', models.URLField(blank=True, default=None, help_text='http://www.my-awesome-event.com', null=True, verbose_name='External URL')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('event_information', ckeditor.fields.RichTextField(blank=True, help_text='Event Information HTML', null=True, verbose_name='Event Information')),
                ('schedule_confirmed', models.BooleanField(default=False, verbose_name='Schedule Confirmed')),
                ('place', models.TextField(verbose_name='Place')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='EventDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(help_text='When will your event be?', verbose_name='Date')),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.Event', verbose_name='Event')),
            ],
        ),
        migrations.CreateModel(
            name='EventUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.Event', verbose_name='Event')),
            ],
            options={
                'verbose_name': 'Event User',
                'verbose_name_plural': 'Event Users',
            },
        ),
        migrations.CreateModel(
            name='EventUserAttendanceDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, help_text='The date of the attendance', verbose_name='Date')),
                ('event_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.EventUser', verbose_name='Event User')),
            ],
        ),
        migrations.CreateModel(
            name='Hardware',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('MOB', 'Mobile'), ('NOTE', 'Notebook'), ('NET', 'Netbook'), ('TAB', 'Tablet'), ('DES', 'Desktop'), ('OTH', 'Other')], max_length=200, verbose_name='Type')),
                ('manufacturer', models.CharField(blank=True, max_length=200, null=True, verbose_name='Manufacturer')),
                ('model', models.CharField(blank=True, max_length=200, null=True, verbose_name='Model')),
            ],
        ),
        migrations.CreateModel(
            name='Installation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.TextField(blank=True, help_text='Any information or trouble you found and consider relevant to document', null=True, verbose_name='Notes')),
                ('attendee', models.ForeignKey(help_text='The owner of the installed hardware', on_delete=django.db.models.deletion.CASCADE, to='manager.Attendee', verbose_name='Attendee')),
                ('hardware', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.Hardware', verbose_name='Hardware')),
                ('installer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='installed_by', to='manager.EventUser', verbose_name='Installer')),
            ],
            options={
                'verbose_name': 'Installation',
                'verbose_name_plural': 'Installations',
            },
        ),
        migrations.CreateModel(
            name='InstallationMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', ckeditor.fields.RichTextField(blank=True, help_text='Email message HTML Body', null=True, verbose_name='Message Body')),
                ('contact_email', models.EmailField(max_length=254, verbose_name='Contact Email')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.Event', verbose_name='Event')),
            ],
            options={
                'verbose_name': 'Post-install Email',
                'verbose_name_plural': 'Post-install Emails',
            },
        ),
        migrations.CreateModel(
            name='Installer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(choices=[('1', 'Beginner'), ('2', 'Medium'), ('3', 'Advanced'), ('4', 'Super Hacker')], help_text='Knowledge level for an installation', max_length=200, verbose_name='Level')),
                ('event_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.EventUser', verbose_name='Event User')),
            ],
            options={
                'verbose_name': 'Installer',
                'verbose_name_plural': 'Installers',
            },
        ),
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.EventUser', verbose_name='Event User')),
            ],
            options={
                'verbose_name': 'Organizer',
                'verbose_name_plural': 'Organizers',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='i.e. Classroom 256', max_length=200, verbose_name='Name')),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.Event', verbose_name='Event')),
            ],
            options={
                'verbose_name': 'Room',
                'ordering': ['name'],
                'verbose_name_plural': 'Rooms',
            },
        ),
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('type', models.CharField(choices=[('OS', 'Operative System'), ('AP', 'Application'), ('SU', 'Support and Problem Fixing'), ('OT', 'Other')], max_length=200, verbose_name='Type')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sent', models.BooleanField(default=False, verbose_name='Sent')),
            ],
        ),
        migrations.AddField(
            model_name='installation',
            name='software',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.Software', verbose_name='Software'),
        ),
        migrations.AddField(
            model_name='eventuser',
            name='ticket',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.Ticket', verbose_name='Ticket'),
        ),
        migrations.AddField(
            model_name='eventuser',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AddField(
            model_name='contactmessage',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.Event', verbose_name='Event'),
        ),
        migrations.AddField(
            model_name='contact',
            name='event',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='manager.Event', verbose_name='Event'),
        ),
        migrations.AddField(
            model_name='contact',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.ContactType', verbose_name='Contact Type'),
        ),
        migrations.AddField(
            model_name='collaborator',
            name='event_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.EventUser', verbose_name='Event User'),
        ),
        migrations.AddField(
            model_name='attendee',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.Event', verbose_name='Event'),
        ),
        migrations.AddField(
            model_name='attendee',
            name='ticket',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.Ticket', verbose_name='Ticket'),
        ),
        migrations.AddField(
            model_name='activity',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.Event', verbose_name='Event'),
        ),
        migrations.AddField(
            model_name='activity',
            name='room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.Room', verbose_name='Room'),
        ),
        migrations.AlterUniqueTogether(
            name='eventuser',
            unique_together=set([('event', 'user')]),
        ),
        migrations.AlterUniqueTogether(
            name='attendee',
            unique_together=set([('event', 'email')]),
        ),
    ]
