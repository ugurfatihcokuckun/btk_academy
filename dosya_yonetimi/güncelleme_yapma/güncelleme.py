"""
with open("newfile.txt", "r+", encoding="utf-8") as file:
   file.seek(20)
   file.write("deneme")

with open("newfile.txt", "r+", encoding="utf-8") as file:
   print(file.read())
"""

"""
# *********** sayfa sonunda güncelleme
with open("newfile.txt", "a", encoding="utf-8") as file:
    file.write("\nEmel Turan")
"""

"""
# *********** sayfa başında güncelleme
with open("newfile.txt", "r+", encoding="utf-8") as file:
   content = file.read()
   content = "Efe Turan\n" + content
   file.seek(0)
   file.write(content)
   print(content)
   
with open("newfile.txt", "r", encoding="utf-8") as file:
   print(file.read())
"""

# *********** sayfa ortasında güncelleme

# with open("newfile.txt", "r+", encoding="utf-8") as file:
#    list = file.readlines()
#    help(list.insert)
#    list.insert(1, "Ali Korkmaz\n")
#    file.seek(0)
#    for i in list:
#       file.write(i)

# with open("newfile.txt", "r", encoding="utf-8") as file:
#    print(file.read())

with open("newfile.txt", "r+", encoding="utf-8") as file:
   list = file.readlines()
   help(list.insert)
   list.insert(1, "Ayşe Korkmaz\n")
   file.seek(0)
   file.writelines(list)

with open("newfile.txt", "r", encoding="utf-8") as file:
   print(file.read())