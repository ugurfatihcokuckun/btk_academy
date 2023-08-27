import mysql.connector
import datetime

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="377AqSwDe",
    database="schooldb"
)

class Student:
    connection = connection
    mycursor = connection.cursor()
    def __init__(self, studentNumber,name,surname,birthdate,gender):
        self.studentNumber = studentNumber
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender

    def saveStudent(self):
        sql = "INSERT INTO Student(StudentNumber,Name,Surname,Birthdate,Gender) VALUES (%s,%s,%s,%s,%s)"
        value = (self.studentNumber,self.name,self.surname,self.birthdate,self.gender)
        Student.mycursor.execute(sql,value)

        try:
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} tane kayıt eklendi")
        except mysql.connector.Error as err:
            print("hata:", err)
        finally:
            Student.connection.close()

    @staticmethod
    def saveStudents(students):
        sql = "INSERT INTO Student(StudentNumber,Name,Surname,Birthdate,Gender) VALUES (%s,%s,%s,%s,%s)"
        values = students
        Student.mycursor.executemany(sql, values)

        try:
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} tane kayıt eklendi")
        except mysql.connector.Error as err:
            print("hata:", err)
        finally:
            Student.connection.close()

# ahmet = Student("202","Ahmet","Yılmaz",datetime.datetime(2005, 3, 10),"E")
# ahmet.saveStudent()


students = [
    ("301","Ahmet","Yılmaz",datetime.datetime(2005, 5, 17),"E"),
    ("302","Ali","Can",datetime.datetime(2005, 6, 17),"E"),
    ("303","Canan","Tan",datetime.datetime(2005, 7, 7),"K"),
    ("304","Ayşe","Taner",datetime.datetime(2005, 9, 23),"K"),
    ("305","Bahadır","Toksöz",datetime.datetime(2004, 7, 27),"E"),
    ("306","Ali","Cenk",datetime.datetime(2003, 8, 25),"E")
]

Student.saveStudents(students)