import datetime

today = datetime.datetime.today()

new_today = today - datetime.timedelta(days=5)

print(new_today)