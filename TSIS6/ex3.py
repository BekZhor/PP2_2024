import os

os.chdir("C:\\Users\\Acer\\Desktop\\Новая папка (2)")

p = os.path.exists(r"C:\Users\Acer\Desktop\Новая папка (2)")

if p :
    print("exists")
    print(os.path.basename(r"C:\Users\Acer\Desktop\Новая папка (2)"))