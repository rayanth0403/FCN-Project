from django.db import models

class student(models.Model):
	cName = models.CharField(max_length=20, null=True)
	cSex = models.CharField(max_length=2, default='M', null=True)
	cBirthday = models.DateField(null=True)
	cEmail = models.EmailField(max_length=100, blank=True, default='')
	cPhone = models.CharField(max_length=50, blank=True, default='')
	cAddr = models.CharField(max_length=255,blank=True, default='')

	def __str__(self):
		return self.cName

class FCN(models.Model):
	cbank = models.CharField(max_length=20, null=True)
	cinvestor = models.CharField(max_length=20, null=True)
	ctradingDay = models.DateField(blank=True)
	creleaseDay = models.DateField(blank=True)
	cexpiryDay = models.DateField(blank=True)
	cransomDay = models.DateField(blank=True)
	cfinalEvaluation = models.DateField(blank=True)
	corder=models.BooleanField(default=True)
	cCND=models.FloatField(blank=True)
	cUSD=models.FloatField(blank=True)
	crate=models.FloatField(blank=True)
	cstock1Exist=models.BooleanField(default=True)
	cstock1=models.CharField(max_length=20, null=True)
	cstock1KOPrice=models.FloatField(blank=True)
	cstock1StartPrice=models.FloatField(blank=True)
	cstock1TranformPrice=models.FloatField(blank=True)
	cstock2Exist=models.BooleanField(default=False)
	cstock2=models.CharField(max_length=20, blank=True)
	cstock2KOPrice=models.FloatField(blank=True)
	cstock2StartPrice=models.FloatField(blank=True)
	cstock2TranformPrice=models.FloatField(blank=True)
	cstock3Exist=models.BooleanField(default=False)
	cstock3=models.CharField(max_length=20, blank=True)
	cstock3KOPrice=models.FloatField(blank=True)
	cstock3StartPrice=models.FloatField(blank=True)
	cstock3TranformPrice=models.FloatField(blank=True)
	cstock4Exist=models.BooleanField(default=False)
	cstock4=models.CharField(max_length=20, blank=True)
	cstock4KOPrice=models.FloatField(blank=True)
	cstock4StartPrice=models.FloatField(blank=True)
	cstock4TranformPrice=models.FloatField(blank=True)
	cobservationTime1=models.DateField(blank=True)
	cobservationTimeEnd1=models.DateField(blank=True)
	cdeliveryDate1=models.DateField(blank=True)
	cobservationTime2=models.DateField(blank=True)
	cobservationTimeEnd2=models.DateField(blank=True)
	cdeliveryDate2=models.DateField(blank=True)
	cobservationTime3=models.DateField(blank=True)
	cobservationTimeEnd3=models.DateField(blank=True)
	cdeliveryDate3=models.DateField(blank=True)
	cobservationTime4=models.DateField(blank=True)
	cobservationTimeEnd4=models.DateField(blank=True)
	cdeliveryDate4=models.DateField(blank=True)
	cobservationTime5=models.DateField(blank=True)
	cobservationTimeEnd5=models.DateField(blank=True)
	cdeliveryDate5=models.DateField(blank=True)
	cobservationTime6=models.DateField(blank=True)
	cobservationTimeEnd6=models.DateField(blank=True)
	cdeliveryDate6=models.DateField(blank=True)
	cobservationTime7=models.DateField(blank=True)
	cobservationTimeEnd7=models.DateField(blank=True)
	cdeliveryDate7=models.DateField(blank=True)
	cobservationTime8=models.DateField(blank=True)
	cobservationTimeEnd8=models.DateField(blank=True)
	cdeliveryDate8=models.DateField(blank=True)
	cobservationTime9=models.DateField(blank=True)
	cobservationTimeEnd9=models.DateField(blank=True)
	cdeliveryDate9=models.DateField(blank=True)
	cobservationTime10=models.DateField(blank=True)
	cobservationTimeEnd10=models.DateField(blank=True)
	cdeliveryDate10=models.DateField(blank=True)
	cobservationTime11=models.DateField(blank=True)
	cobservationTimeEnd11=models.DateField(blank=True)
	cdeliveryDate11=models.DateField(blank=True)
	cobservationTime12=models.DateField(blank=True)
	cobservationTimeEnd12=models.DateField(blank=True)
	cdeliveryDate12=models.DateField(blank=True)
