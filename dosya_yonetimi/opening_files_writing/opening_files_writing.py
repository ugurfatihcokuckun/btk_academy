# Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır.
# kullanımı: open(dosya_adi, dosya_erişme_modu)
# dosya_erişme_modu => dosyayı hangi amaçla açtığımızı belirtir.

# "w": (Write) yazma modu. Dosyayı konumda oluşturur. **Mevcutta bir dosya varsa dosya içeriğini siler ve yeniden düzenler.

"""
file = open("newfile2.txt","w")
file.close()
"""

"""
file = open("C:/Users/Fatih/Desktop/newfile.txt", "w")
file.close()
"""

"""
file = open("newfile2.txt","w", encoding="utf-8")
file.write("Fatih Çokuçkun")
file.close()
"""

# "a": (Append) ekleme. Dosya konumda yoksa oluşturur.

"""
file = open("newfile2.txt","a", encoding="utf-8")
file.write("\nFatih Çokuçkun")
file.close()
"""

# "x": (Create) oluşturma. Dosya zaten varsa hata verir.

"""
file = open("newfile3.txt","x", encoding="utf-8")
"""

# "r": (Read) okuma. varsayılan. Dosya konumda yoksa hata verir. 

"""
file = open("newfile2.txt", "r")
print(file)
"""

"""
try:
    file = open("newfile5.txt", "r")
    print(file)
except FileNotFoundError:
    print("dosya okuma hatası")
finally:
    print("dosya kapandı.")
    file.close()
"""

file = open("newfile.txt", "r", encoding= "utf-8")
"""
# for döngüsü
for i in file:
    print(i, end="")
file.close()
"""

"""
# *********** read() fonksiyon
content1 = file.read()

print("içerik 1")
print(content1)

file = open("newfile.txt", "r", encoding= "utf-8")
content2 = file.read()

print("içerik 2")
print(content2)

file.close()
"""

"""
content = file.read(5)
content = file.read(8)
print(content)
file.close()
"""

"""
# *********** readline() fonksiyon

print(file.readline(), end = "")
print(file.readline(), end = "")
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
"""

"""
# *********** readlines() fonksiyon

liste = file.readlines()
print(liste)
print(liste[1])
"""

