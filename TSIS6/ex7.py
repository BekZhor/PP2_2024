os.chdir("C:\\Users\\Acer\\Desktop\\Новая папка (2)")
exists = os.access("C:\\Users\\Acer\\Desktop\\Новая папка (2)", os.F_OK)
print(exists)

if exists :
    os.remove("abobik")