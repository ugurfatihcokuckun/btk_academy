import os 
import datetime

result = dir(os)
result = os.name

# os.chdir("..")  #dizin değiştirme
result = os.getcwd()  #dosyanın olduğu konum
# os.mkdir("new")  #klasör oluşturur
# os.makedirs("new/neww")
# os.rename("new", "new3")
# os.rmdir("new3")  #alt dizini yoksa klasörü siler
# os.removedirs("new", "neww")  #alt dizinleri siler
# result = os.listdir()
# result = os.listdir("C:\\")
# for dosya in os.listdir():
#     if dosya.endswith(".py"):
#         print(dosya)

result = os.stat("os.py")
# result = result.st_size  # byte cinsinden dosya boyutu "/1024 kb"
# result = result.st_ctime
# result = datetime.datetime.fromtimestamp(result.st_ctime)  #dosyanın oluşturulma zamanı
# result = datetime.datetime.fromtimestamp(result.st_atime)  # son erişilme tarihi
# result = datetime.datetime.fromtimestamp(result.st_ctime)  #değiştirlme tarihi
# os.system("notepad.exe")  # notepadi açar

result = os.path.abspath("_os.py")
result = os.path.dirname("C:/Users/Fatih/Desktop/btk academy/ileri_seviye_modüller/os/_os.py")
result = os.path.dirname(os.path.abspath("os.py"))
result = os.path.exists("os.py")
result = os.path.exists("C:/Users/Fatih/Desktop/btk academy/ileri_seviye_modüller")
result = os.path.isdir("")  # klasör mü değil mi
result = os.path.isfile("")  # dosya mı değil mi
result = os.path.join("C://")  # sadece yol oluşturur


print(result)

