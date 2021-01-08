# PE2
# 4.6.1.1 The calendar module

# setfirstweekday() function
import calendar

calendar.setfirstweekday(calendar.SUNDAY)
calendar.prmonth(2020, 12)

print() # weekday() function
print(calendar.weekday(2020, 12, 24))

print() # isleap() function, leapdays() function
print(calendar.isleap(2020))
print(calendar.leapdays(2010, 2021)) # up to but not including 2021
