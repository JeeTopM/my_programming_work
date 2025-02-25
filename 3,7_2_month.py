import calendar

en_months = list(calendar.month_abbr)
s = input().split(" ")
y, m = int(s[0]), s[1]
ind_m = en_months.index(m)
print(calendar.month(y, ind_m))
