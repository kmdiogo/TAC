# Generated by Django 2.1.2 on 2018-10-18 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SignIn', '0002_auto_20181014_1248'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='academicYear',
            field=models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JU', 'Junior'), ('SR', 'Senior')], max_length=2, null=True, verbose_name='Academic Year'),
        ),
        migrations.AddField(
            model_name='student',
            name='dob',
            field=models.DateField(null=True, verbose_name='Date of Birth'),
        ),
        migrations.AddField(
            model_name='student',
            name='major',
            field=models.CharField(choices=[('ACCT', 'Accounting'), ('ADV', 'Advertising'), ('AERO', 'Aerospace Studies'), ('AFST', 'Africana Studies'), ('AHLT', 'Allied Health'), ('ASL', 'American Sign Language'), ('AMER', 'American Studies'), ('ANTH', 'Anthropology'), ('ARBC', 'Arabic'), ('ART', 'Art'), ('ASTR', 'Astronomy'), ('BIOL', 'Biology'), ('BUS', 'Business Administration'), ('CHEN', 'Chemical Engineering'), ('CHEM', 'Chemistry'), ('CHFM', 'Child and Family'), ('CHIN', 'Chinese'), ('CCET', 'Civil and Constructn Engr Tech'), ('CEEN', 'Civil and Environmental Engr'), ('CMST', 'Communication Studies'), ('CIS', 'Computer Information Systems'), ('CSCI', 'Computer Science'), ('CSIS', 'Computer Science Informtn Sys'), ('COUN', 'Counseling'), ('CCAC', 'Creative Arts & Communication'), ('CJFS', 'Criminal Just and Forensic Sci'), ('DNCE', 'Dance'), ('DHYG', 'Dental Hygiene'), ('ECE', 'Early Childhood Education'), ('ECIS', 'Early Chld Interven Specialist'), ('ECON', 'Economics'), ('EDAD', 'Educational Administration'), ('EDFN', 'Educational Foundations'), ('EUT', 'Electric Utility Tech'), ('EET', 'Electrical Engineering Tech'), ('ECEN', 'Electrical and Computer Engr'), ('EMS', 'Emergency Medical Services'), ('ENGR', 'Engineering'), ('ENTC', 'Engineering Technology'), ('ENGL', 'English'), ('ENT', 'Entrepreneurship'), ('ENST', 'Environmental Studies'), ('FIN', 'Finance'), ('FNUT', 'Food and Nutrition'), ('FNLG', 'Foreign Language'), ('FOUN', 'Foundations of Education'), ('FRNC', 'French'), ('GEOG', 'Geography'), ('GEOL', 'Geology'), ('GERO', 'Gerontology'), ('GRK', 'Greek'), ('HEPE', 'Health Educ Physical Educ'), ('HAHS', 'Health and Human Serv College'), ('HHS', 'Health and Human Services'), ('HIST', 'History'), ('HONR', 'Honors'), ('HMGT', 'Hospitality Management'), ('HMEC', 'Human Ecology'), ('ISEN', 'Industrial And Systems Engr'), ('INFO', 'Information Technology'), ('ITAL', 'Italian'), ('JOUR', 'Journalism'), ('JUDC', 'Judaic Studies'), ('KSS', 'Kinesiology and Sport Science'), ('LATN', 'Latin'), ('LASS', 'Liberal Arts and Social Sci'), ('MGT', 'Management'), ('MKTG', 'Marketing'), ('MBA', 'Master Business Administration'), ('MPH', 'Master in Public Health'), ('MAT', 'Master of Athletic Training'), ('MTEN', 'Materials Engineering'), ('MATL', 'Materials Science'), ('MATH', 'Mathematics'), ('MECH', 'Mechanical Engineering'), ('MET', 'Mechanical Engineering Tech'), ('MATC', 'Medical Assisting Technology'), ('MLS', 'Medical Laboratory Science'), ('MLT', 'Medical Laboratory Technology'), ('MRCH', 'Merch Fashion and Interiors'), ('MSCI', 'Military Science'), ('BHRN', 'Music Appl Lesson Baritone Hrn'), ('BASS', 'Music Appl Lesson Bassoon'), ('CELL', 'Music Appl Lesson Cello'), ('CLAR', 'Music Appl Lesson Clarinet'), ('MCMP', 'Music Appl Lesson Composition'), ('CNDC', 'Music Appl Lesson Conducting'), ('FLUT', 'Music Appl Lesson Flute'), ('FHRN', 'Music Appl Lesson French Horn'), ('GUIT', 'Music Appl Lesson Guitar'), ('OBOE', 'Music Appl Lesson Oboe'), ('ORGN', 'Music Appl Lesson Organ'), ('PERC', 'Music Appl Lesson Percussion'), ('PIAN', 'Music Appl Lesson Piano'), ('SAX', 'Music Appl Lesson Saxophone'), ('SBSS', 'Music Appl Lesson String Bass'), ('TROM', 'Music Appl Lesson Trombone'), ('TRUM', 'Music Appl Lesson Trumpet'), ('TUBA', 'Music Appl Lesson Tuba'), ('VIOL', 'Music Appl Lesson Viola'), ('VION', 'Music Appl Lesson Violin'), ('VOIC', 'Music Appl Lesson Voice'), ('MUAC', 'Music Applied Classes'), ('MUCO', 'Music Conducting'), ('MUED', 'Music Education'), ('MUEN', 'Music Ensembles'), ('MUHL', 'Music History and Literature'), ('MUIN', 'Music Industry'), ('MUTC', 'Music Theory and Composition'), ('NURS', 'Nursing'), ('PHIL', 'Philosophy'), ('PHYT', 'Physical Therapy'), ('PHYS', 'Physics'), ('POL', 'Political Science'), ('PSYC', 'Psychology'), ('PHLT', 'Public Health'), ('RSS', 'Reading and Study Skills'), ('REL', 'Religious Studies'), ('RESC', 'Respiratory Care'), ('SPSY', 'School Psychology'), ('STEM', 'Science Tech Engineering Math'), ('SED', 'Secondary Education'), ('SCWK', 'Social Work'), ('SOC', 'Sociology'), ('SPAN', 'Spanish'), ('SPED', 'Special Education'), ('STAT', 'Statistics'), ('TEMC', 'Teacher Educ Middle Childhood'), ('TCED', 'Teacher Education'), ('TERG', 'Teacher Education Reading'), ('TCOM', 'Telecommunication Studies'), ('THTR', 'Theatre'), ('WMST', 'Womens Studies')], max_length=50, null=True, verbose_name='Major'),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='student',
            name='firstName',
            field=models.CharField(max_length=50, null=True, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='student',
            name='lastName',
            field=models.CharField(max_length=50, null=True, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='student',
            name='sex',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True, verbose_name='Sex'),
        ),
    ]