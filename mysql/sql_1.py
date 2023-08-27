import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "377AqSwDe",
    database="schooldb"
)

def insertProduct(name,price,imageUrl,description):
    connection = mysql.connector.connect(host="localhost",user="root",password="377AqSwDe",database="node-app")
    cursor = connection.cursor()

    sql = "INSERT INTO products (name,price,imageUrl,description) VALUES (%s,%s,%s,%s)"
    values = (name,price,imageUrl,description)

    cursor.execute(sql,values)
    try:
        connection.commit()
        print(f"{cursor.rowcount} tane kayıt eklendi")
        print(f"son eklenen kaydın id:{cursor.lastrowid}")
    except mysql.connector.Error as err:
        print("hata",err)
    finally:
        connection.close()
        print("database bağlantısı kapandı")


def insertProducts(list):
    connection = mysql.connector.connect(host="localhost",user="root",password="377AqSwDe",database="node-app")
    cursor = connection.cursor()

    sql = "INSERT INTO products (name,price,imageUrl,description) VALUES (%s,%s,%s,%s)"
    values = list

    cursor.executemany(sql,values)
    try:
        connection.commit()
        print(f"{cursor.rowcount} tane kayıt eklendi")
        print(f"son eklenen kaydın id:{cursor.lastrowid}")
    except mysql.connector.Error as err:
        print("hata",err)
    finally:
        connection.close()
        print("database bağlantısı kapandı")


def getProducts():
    connection = mysql.connector.connect(host="localhost",user="root",password="377AqSwDe",database="node-app")
    cursor = connection.cursor()

    #cursor.execute("SELECT * From Products")
    cursor.execute("SELECT name,price From Products")
    result = cursor.fetchall()
    for product in result:
        #print(product)
        print(f"name: {product[0]} price: {product[1]}")

getProducts()

list = []

while True:
    name = input("ürün adı: ")
    price = input("ürün fiyatı: ")
    imageUrl = input("ürün image: ")
    description = input("ürün açıklaması: ")

    list.append((name,price,imageUrl,description))

    result = input("Devam etmek istiyor musunuz? (e/h)")
    if result == "h":
        print("Kayıtlarınız veri tabanına aktarılıyor...")
        print(list)
        insertProducts(list)
        break
#insertProduct(name,price,imageUrl,description)