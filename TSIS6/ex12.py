import time, math
sq, t = int(input("Input the value: ")), int(input("Input waiting time: "))
time.sleep(t / 1000)
num = math.sqrt(sq)
print("The square root of", sq, "after", t, "miliseconds is", num)