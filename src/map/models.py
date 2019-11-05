from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.timezone import now
import datetime

# Create your models here.
class News(models.Model):
    CRIME_CATEGORY = (
        ('WAR', 'WARRANTS'), 
        ('OTH', 'OTHER OFFENSES'), 
        ('LAR', 'LARCENY/THEFT'), 
        ('VEH', 'VEHICLE THEFT'), 
        ('VAN', 'VANDALISM'), 
        ('NON', 'NON-CRIMINAL'), 
        ('ROB', 'ROBBERY'), 
        ('AS', 'ASSAULT'), 
        ('WEA', 'WEAPON LAWS'), 
        ('BUR', 'BURGLARY'), 
        ('SUS', 'SUSPICIOUS OCC'), 
        ('DRU', 'DRUNKENNESS'), 
        ('FOR', 'FORGERY/COUNTERFEITING'), 
        ('NAR', 'DRUG/NARCOTIC'), 
        ('STO', 'STOLEN PROPERTY'), 
        ('SEC', 'SECONDARY CODES'), 
        ('TRE', 'TRESPASS'), 
        ('MIS', 'MISSING PERSON'), 
        ('FR', 'FRAUD'), 
        ('KID', 'KIDNAPPING'), 
        ('RUN', 'RUNAWAY'), 
        ('DRI', 'DRIVING UNDER THE INFLUENCE'), 
        ('SOF', 'SEX OFFENSES FORCIBLE'), 
        ('PRO', 'PROSTITUTION'), 
        ('DIS', 'DISORDERLY CONDUCT'), 
        ('ARS', 'ARSON'), 
        ('FAM', 'FAMILY OFFENSES'), 
        ('LIQ', 'LIQUOR LAWS'), 
        ('BRI', 'BRIBERY'), 
        ('EMB', 'EMBEZZLEMENT'), 
        ('SUI', 'SUICIDE'), 
        ('LOI', 'LOITERING'), 
        ('SONF', 'SEX OFFENSES NON FORCIBLE'), 
        ('EXT', 'EXTORTION'), 
        ('GAM', 'GAMBLING'), 
        ('BC', 'BAD CHECKS'), 
        ('TE', 'TREA'), 
        ('RV', 'RECOVERED VEHICLE'), 
        ('POR', 'PORNOGRAPHY/OBSCENE MAT'),
    )
    title = models.CharField(max_length=60)
    category = models.CharField(max_length=55,choices=CRIME_CATEGORY)
    severity = models.IntegerField(default=1,validators=[
        MaxValueValidator(5),
        MinValueValidator(1)
    ])
    state = models.CharField(max_length=35)
    statecode = models.CharField(max_length=2)
    city = models.CharField(max_length=40)
    time_created = models.DateTimeField(
        default=now, blank=True, editable=True)

    # ensures only new news data is displayed
    def older_than_ten_days(self):
        ten_days_ago = (now() - datetime.timedelta(days=10)).timestamp()
        return ten_days_ago >= self.time_created.timestamp()
