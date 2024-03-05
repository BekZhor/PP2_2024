import datetime
today = datetime.datetime.now()
today_seconds = today.timestamp()

any_data = datetime.datetime(2024,2,16,10,12,10)
any_data_seconds = any_data.timestamp()

print(abs(today_seconds - any_data_seconds))