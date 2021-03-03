import calendar
m,d,y=map(int,input().split())
a=list(calendar.day_name)
b=calendar.weekday(y,m,d)
print(a[b].upper())