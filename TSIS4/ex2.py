import datetime

today = datetime.datetime.today()

new_today = today - datetime.timedelta(days=1)
new_today1 = today + datetime.timedelta(days=1)

print(today)
print(new_today)
print(new_today1)