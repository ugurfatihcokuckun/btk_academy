
"""
try:
    x = int(input("x: "))
    y = int(input("y: "))
    print(x/y)
except ZeroDivisionError:
    print("y için 0 girilemez")
except ValueError:
    print("x ve y için sayısal değer girmelisiniz")
"""
"""
try:
    x = int(input("x: "))
    y = int(input("y: "))
    print(x/y)
except (ZeroDivisionError, ValueError):
    print("Yanlış bilgi girdiniz")
"""
"""
try:
    x = int(input("x: "))
    y = int(input("y: "))
    print(x/y)
except (ZeroDivisionError, ValueError) as e:
    print("Yanlış bilgi girdiniz")
    print(e)
"""
"""
try:
    x = int(input("x: "))
    y = int(input("y: "))
    print(x/y)
except:
    print("Yanlış bilgi girdiniz")
"""
"""
try:
    x = int(input("x: "))
    y = int(input("y: "))
    print(x/y)
except:
    print("Yanlış bilgi girdiniz")
else:
    print("her şey yolunda")
"""
"""
while True:
    try:
        x = int(input("x: "))
        y = int(input("y: "))
        print(x/y)
    except:
        print("Yanlış bilgi girdiniz")
    else:
        break
"""
"""
while True:
    try:
        x = int(input("x: "))
        y = int(input("y: "))
        print(x/y)
    except Exception as ex:
        print("Yanlış bilgi girdiniz", ex)
    else:
        break
"""

while True:
    try:
        x = int(input("x: "))
        y = int(input("y: "))
        print(x/y)
    except Exception as ex:
        print("Yanlış bilgi girdiniz", ex)
    else:
        break
    finally:
        print("try except sonlandı.")