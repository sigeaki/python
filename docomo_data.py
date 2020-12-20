import datetime
import calendar
n=float(input("今日までのデータ使用量は？:"))
ddn=datetime.datetime.now()
Day=ddn.day
Mon=ddn.month
N=n/Day
_, ld = calendar.monthrange(ddn.year,Mon)
print("{}日までの平均データ使用量は{:.2f}".format(Day,N))
print("{}月のデータ使用量の予定は{:.2f}".format(Mon,N*ld))
