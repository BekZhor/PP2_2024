import datetime

print(dir(datetime))

x=datetime.datetime.now()

y=x-datetime.timedelta(days=5)

z=x-y

print(x)

print(y)