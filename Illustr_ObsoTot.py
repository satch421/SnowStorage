NumberHosp = 18

NumberSnow = 3
DaysperHosp = 2
OneTimeSnowFee = 300
SnowLateDayRate = 30
DaysPerOneSnow = 10
TeraBperSnow = 80
S3costperTera = 23.5
S3InfrCostperTera = 12.5
S3GlacDeepCostperTera = 5
PercTotS3Store = .1
PercTotInfAcc = .15
PercTotStorage = 1
PercTotGlacDeep = PercTotStorage - PercTotInfAcc - PercTotS3Store

InstallDays = 10
dayrate = 1150

TotStorage = TeraBperSnow * NumberSnow
PercTotGlacDeep = PercTotStorage - PercTotS3Store - PercTotInfAcc
CostS3Storage = TotStorage * PercTotS3Store * S3costperTera
CostInfAccess = TotStorage * PercTotInfAcc * S3InfrCostperTera
CostGlacDeep = TotStorage * PercTotGlacDeep * S3GlacDeepCostperTera

TotBackupDays = NumberHosp * DaysperHosp
TotLateSnowDays = TotBackupDays - DaysPerOneSnow * NumberSnow
TotLateSnowCharge = TotLateSnowDays * SnowLateDayRate
TotOneTimeSnowFee = OneTimeSnowFee * NumberSnow
TotSnowfees = TotOneTimeSnowFee + TotLateSnowCharge

TotAWSfees = TotSnowfees + CostS3Storage + CostInfAccess + CostGlacDeep

days = InstallDays + TotBackupDays
pay = days * dayrate

TotEngageFees = TotAWSfees + pay


print(CostS3Storage)
print(CostInfAccess)
print(CostGlacDeep)
print("----------------------------")
print(TotSnowfees)
print(TotAWSfees)
print("----------------------------")
print(pay)

print(TotEngageFees)
