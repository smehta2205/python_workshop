import datetime

d =  datetime.datetime.today()
print(d)

year = d.year
print(year)
month = d.month
print(month)
day = d.day
print(day)
hour = d.hour
print(hour)
d1 = datetime.datetime(2017, 4, 19)
print(d1)

x = datetime.datetime.today() - datetime.datetime(2017, 4 , 19, 0, 1, 0)
print(x)
