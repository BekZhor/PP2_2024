import os


os.chdir("C:\\Users\\Acer\\Desktop\\Новая папка (2)")


p = os.access("aboba.txt", os.F_OK)
print(p)


p = os.access("aboba.txt", os.R_OK)
print(p)


p = os.access("aboba.txt", os.W_OK)
print(p)


p = os.access("aboba.txt", os.X_OK) 
print(p)