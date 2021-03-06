# --------------------UNIVERSITY CONSTANTS-----------------------------------
SCHOOL_ID_ALIAS = "Y Number"
EMPLOYEE_ID_ALIAS = "Y Number"
SCHOOL_ID_REGEX = 'Y00\d{6}'
EMPLOYEE_ID_REGEX = 'Y00\d{6}'
DOW_ALLOWED_MIN = 1
DOW_ALLOWED_MAX = 5
# ---------------------------------------------------------------------------
# --------------------PROGRAMMING CONSTANTS----------------------------------
ERROR_OPEN_OBJECT = 1
ERROR_PERSON_DNE = 2
ERROR_BAD__DATA = 3
DOW_DICT = {0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday'}
STATUS_DICT = {0: 'Pending', 1: 'Approved', 2: 'Denied'}
# ---------------------------------------------------------------------------
# -------------------CHOICE TUPLES FOR FIELDS--------------------------------
SEX_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female')
)
CLASS_CHOICES = (
    ('FR', 'Freshman'),
    ('SO', 'Sophomore'),
    ('JU', 'Junior'),
    ('SR', 'Senior')
)
MAJOR_CHOICES = (
    ('ACCT', 'Accounting'),
    ('ADV', 'Advertising'),
    ('AERO', 'Aerospace Studies'),
    ('AFST', 'Africana Studies'),
    ('AHLT', 'Allied Health'),
    ('ASL', 'American Sign Language'),
    ('AMER', 'American Studies'),
    ('ANTH', 'Anthropology'),
    ('ARBC', 'Arabic'),
    ('ART', 'Art'),
    ('ASTR', 'Astronomy'),
    ('BIOL', 'Biology'),
    ('BUS', 'Business Administration'),
    ('CHEN', 'Chemical Engineering'),
    ('CHEM', 'Chemistry'),
    ('CHFM', 'Child and Family'),
    ('CHIN', 'Chinese'),
    ('CCET', 'Civil and Constructn Engr Tech'),
    ('CEEN', 'Civil and Environmental Engr'),
    ('CMST', 'Communication Studies'),
    ('CIS', 'Computer Information Systems'),
    ('CSCI', 'Computer Science'),
    ('CSIS', 'Computer Science Informtn Sys'),
    ('COUN', 'Counseling'),
    ('CCAC', 'Creative Arts & Communication'),
    ('CJFS', 'Criminal Just and Forensic Sci'),
    ('DNCE', 'Dance'),
    ('DHYG', 'Dental Hygiene'),
    ('ECE', 'Early Childhood Education'),
    ('ECIS', 'Early Chld Interven Specialist'),
    ('ECON', 'Economics'),
    ('EDAD', 'Educational Administration'),
    ('EDFN', 'Educational Foundations'),
    ('EUT', 'Electric Utility Tech'),
    ('EET', 'Electrical Engineering Tech'),
    ('ECEN', 'Electrical and Computer Engr'),
    ('EMS', 'Emergency Medical Services'),
    ('ENGR', 'Engineering'),
    ('ENTC', 'Engineering Technology'),
    ('ENGL', 'English'),
    ('ENT', 'Entrepreneurship'),
    ('ENST', 'Environmental Studies'),
    ('FIN', 'Finance'),
    ('FNUT', 'Food and Nutrition'),
    ('FNLG', 'Foreign Language'),
    ('FOUN', 'Foundations of Education'),
    ('FRNC', 'French'),
    ('GEOG', 'Geography'),
    ('GEOL', 'Geology'),
    ('GERO', 'Gerontology'),
    ('GRK', 'Greek'),
    ('HEPE', 'Health Educ Physical Educ'),
    ('HAHS', 'Health and Human Serv College'),
    ('HHS', 'Health and Human Services'),
    ('HIST', 'History'),
    ('HONR', 'Honors'),
    ('HMGT', 'Hospitality Management'),
    ('HMEC', 'Human Ecology'),
    ('ISEN', 'Industrial And Systems Engr'),
    ('INFO', 'Information Technology'),
    ('ITAL', 'Italian'),
    ('JOUR', 'Journalism'),
    ('JUDC', 'Judaic Studies'),
    ('KSS', 'Kinesiology and Sport Science'),
    ('LATN', 'Latin'),
    ('LASS', 'Liberal Arts and Social Sci'),
    ('MGT', 'Management'),
    ('MKTG', 'Marketing'),
    ('MBA', 'Master Business Administration'),
    ('MPH', 'Master in Public Health'),
    ('MAT', 'Master of Athletic Training'),
    ('MTEN', 'Materials Engineering'),
    ('MATL', 'Materials Science'),
    ('MATH', 'Mathematics'),
    ('MECH', 'Mechanical Engineering'),
    ('MET', 'Mechanical Engineering Tech'),
    ('MATC', 'Medical Assisting Technology'),
    ('MLS', 'Medical Laboratory Science'),
    ('MLT', 'Medical Laboratory Technology'),
    ('MRCH', 'Merch Fashion and Interiors'),
    ('MSCI', 'Military Science'),
    ('BHRN', 'Music Appl Lesson Baritone Hrn'),
    ('BASS', 'Music Appl Lesson Bassoon'),
    ('CELL', 'Music Appl Lesson Cello'),
    ('CLAR', 'Music Appl Lesson Clarinet'),
    ('MCMP', 'Music Appl Lesson Composition'),
    ('CNDC', 'Music Appl Lesson Conducting'),
    ('FLUT', 'Music Appl Lesson Flute'),
    ('FHRN', 'Music Appl Lesson French Horn'),
    ('GUIT', 'Music Appl Lesson Guitar'),
    ('OBOE', 'Music Appl Lesson Oboe'),
    ('ORGN', 'Music Appl Lesson Organ'),
    ('PERC', 'Music Appl Lesson Percussion'),
    ('PIAN', 'Music Appl Lesson Piano'),
    ('SAX', 'Music Appl Lesson Saxophone'),
    ('SBSS', 'Music Appl Lesson String Bass'),
    ('TROM', 'Music Appl Lesson Trombone'),
    ('TRUM', 'Music Appl Lesson Trumpet'),
    ('TUBA', 'Music Appl Lesson Tuba'),
    ('VIOL', 'Music Appl Lesson Viola'),
    ('VION', 'Music Appl Lesson Violin'),
    ('VOIC', 'Music Appl Lesson Voice'),
    ('MUAC', 'Music Applied Classes'),
    ('MUCO', 'Music Conducting'),
    ('MUED', 'Music Education'),
    ('MUEN', 'Music Ensembles'),
    ('MUHL', 'Music History and Literature'),
    ('MUIN', 'Music Industry'),
    ('MUTC', 'Music Theory and Composition'),
    ('NURS', 'Nursing'),
    ('PHIL', 'Philosophy'),
    ('PHYT', 'Physical Therapy'),
    ('PHYS', 'Physics'),
    ('POL', 'Political Science'),
    ('PSYC', 'Psychology'),
    ('PHLT', 'Public Health'),
    ('RSS', 'Reading and Study Skills'),
    ('REL', 'Religious Studies'),
    ('RESC', 'Respiratory Care'),
    ('SPSY', 'School Psychology'),
    ('STEM', 'Science Tech Engineering Math'),
    ('SED', 'Secondary Education'),
    ('SCWK', 'Social Work'),
    ('SOC', 'Sociology'),
    ('SPAN', 'Spanish'),
    ('SPED', 'Special Education'),
    ('STAT', 'Statistics'),
    ('TEMC', 'Teacher Educ Middle Childhood'),
    ('TCED', 'Teacher Education'),
    ('TERG', 'Teacher Education Reading'),
    ('TCOM', 'Telecommunication Studies'),
    ('THTR', 'Theatre'),
    ('WMST', 'Womens Studies')
)

COURSE_CHOICES = (
    ('MATH 1505', 'MATH 1505 - INTERMEDIATE ALGEBRA WITH APPS'),
    ('MATH 1507', 'MATH 1507 - INTERMEDIATE ALGEBRA'),
    ('MATH 1510', 'MATH 1510 - COLLEGE ALGEBRA'),
    ('MATH 1511', 'MATH 1511 - TRIGONOMETRY'),
    ('MATH 1513', 'MATH 1513 - PRE CALCULUS'),
    ('MATH 1552', 'MATH 1552 - BUSINESS CALCULUS (APPLIED MATH FOR MANAGEMENT)'),
    ('MATH 2623', 'MATH 2623 - QUANTITATIVE REASONING'),
    ('MATH 2623H', 'MATH 2623H - HONORS QUANTITATIVE REASONING'),
    ('MATH 1571', 'MATH 1571 - CALCULUS 1'),
    ('MATH 1572', 'MATH 1572 - CALCULUS 2'),
    ('MATH 2673', 'MATH 2673 - CALCULUS 3'),
    ('MATH 1570', 'MATH 1570 - APPLIED CALCULUS 1'),
    ('MATH 2670', 'MATH 2670 - APPLIED CALCULUS 2'),
    ('MATH 2651', 'MATH 2651 - MATH FOR EARLY CHILDHOOD TEACHERS 1'),
    ('MATH 2652', 'MATH 2652 - MATH FOR EARLY CHILDHOOD TEACHERS 2'),
    ('MATH 1564', 'MATH 1564 - FOUNDATIONS OF MIDDLE SCHOOL MATH 1'),
    ('MATH 2665', 'MATH 2665 - FOUNDATIONS OF MIDDLE SCHOOL MATH 2'),
    ('MATH 1585H', 'MATH 1585H - ACCELERATED HONORS CALCULUS 1'),
    ('MATH 2686H', 'MATH 2686H - ACCELERATED HONORS CALCULUS 2'),
    ('MATH 1571H', 'MATH 1571H - HONORS CALCULUS 1'),
    ('MATH 1586H', 'MATH 1586H - HONORS CALCULUS 1 LAB'),
    ('MATH 1572H', 'MATH 1572H - HONORS CALCULUS 2'),
    ('MATH 2687H', 'MATH 2687H - HONORS CALCULUS 2 LAB'),
    ('MATH 2673H', 'MATH 2673H - HONORS CALCULUS 3'),
    ('MATH 1580H', 'MATH 1580H - HONORS BIOMATHEMATICS 1'),
    ('MATH 1581H', 'MATH 1581H - HONORS BIOMATHEMATICS 2'),
    ('MATH 3705', 'MATH 3705 - DIFFERENTIAL EQUATIONS'),
    ('MATH 3705H', 'MATH 3705H - HONORS DIFFERENTIAL EQUATIONS'),
    ('MATH 3715', 'MATH 3715 - DISCRETE MATHEMATICS'),
    ('MATH 3720', 'MATH 3720 - LINEAR ALGEBRA'),
    ('MATH 3715', 'MATH 3715 - DISCRETE MATHEMATICS'),
    ('STAT 2601', 'STAT 2601 - INTRODUCTORY STATISTICS'),
    ('STAT 2625', 'STAT 2625 - STATISTICS LITERACY & CRITICAL REASONING'),
    ('STAT 3717', 'STAT 3717 - STATISTICAL METHODS'),
    ('STAT 3743', 'STAT 3743 - PROBABILITY AND STATISTICS'),
    ('OTHER', 'OTHER - OTHER COURSE NOT LISTED')
)

COURSE_COLORS = {
    "MATH 1505": "rgba(123,3,114,1)",
    "MATH 1507": "rgba(74,249,35,1)",
    "MATH 1510": "rgba(222,232,247,1)",
    "MATH 1511": "rgba(212,50,89,1)",
    "MATH 1513": "rgba(1,197,93,1)",
    "MATH 1552": "rgba(120,137,250,1)",
    "MATH 2623": "rgba(12,37,78,1)",
    "MATH 2623H": "rgba(81,148,87,1)",
    "MATH 1571": "rgba(88,158,140,1)",
    "MATH 1572": "rgba(245,90,69,1)",
    "MATH 2673": "rgba(185,199,172,1)",
    "MATH 1570": "rgba(162,130,216,1)",
    "MATH 2670": "rgba(255,249,50,1)",
    "MATH 2651": "rgba(203,59,132,1)",
    "MATH 2652": "rgba(157,168,196,1)",
    "MATH 1564": "rgba(100,151,60,1)",
    "MATH 2665": "rgba(45,171,116,1)",
    "MATH 1585H": "rgba(26,105,160,1)",
    "MATH 2686H": "rgba(160,133,237,1)",
    "MATH 1571H": "rgba(77,31,43,1)",
    "MATH 1586H": "rgba(130,205,250,1)",
    "MATH 1572H": "rgba(237,174,178,1)",
    "MATH 2687H": "rgba(87,134,26,1)",
    "MATH 2673H": "rgba(67,51,165,1)",
    "MATH 1580H": "rgba(243,253,203,1)",
    "MATH 1581H": "rgba(88,178,103,1)",
    "MATH 3705": "rgba(73,207,153,1)",
    "MATH 3705H": "rgba(119,69,31,1)",
    "MATH 3715": "rgba(2,113,48,1)",
    "MATH 3720": "rgba(116,73,109,1)",
    "MATH 3715": "rgba(68,168,53,1)",
    "STAT 2601": "rgba(43,238,90,1)",
    "STAT 2625": "rgba(117,191,11,1)",
    "STAT 3717": "rgba(33,235,123,1)",
    "STAT 3743": "rgba(113,238,2,1)",
    "OTHER": "rgba(186,225,3,1)",
}