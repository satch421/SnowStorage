NumberHosp = 18

NumberSnow = 3
DaysperHosp = 2
OneTimeSnowFee = 300
SnowLateDayRate = 30
DaysPerOneSnow = 10
TeraBperSnow = 80

InstallDays = 10
dayrate = 980

TotStorage = TeraBperSnow * NumberSnow

TotBackupDays = NumberHosp * DaysperHosp
TotLateSnowDays = TotBackupDays - DaysPerOneSnow * NumberSnow
TotLateSnowCharge = TotLateSnowDays * SnowLateDayRate
TotOneTimeSnowFee = OneTimeSnowFee * NumberSnow
TotAWSfees = TotOneTimeSnowFee + TotLateSnowCharge

days = InstallDays + TotBackupDays
pay = days * dayrate

TotEngageFees = TotAWSfees + pay

print(TotAWSfees)
print(TotStorage)

print(pay)

print(TotEngageFees)
