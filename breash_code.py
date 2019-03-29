import datetime

def next_weekday(d, weekday):
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0: # Target day already happened this week
        days_ahead += 7
    return d + datetime.timedelta(days_ahead)

d = datetime.datetime.now()
next_wednesday = next_weekday(d, 2) # 0 = Monday, 1=Tuesday, 2=Wednesday...
next_wednesday_str = next_wednesday.strftime('%Y.%m.%d')
print(next_wednesday_str)
