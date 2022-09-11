import pymysql


# Открыть соединение с базой данных
db = pymysql.connect(«localhost», «root», «пароль», «RUNOOB»)
 # Используйте метод cursor () для создания курсора объекта курсора
cursor = db.cursor()

 # Используйте метод execute () для выполнения SQL-запроса
cursor.execute("SELECT VERSION()")
 # Используйте метод fetchone () для получения одного фрагмента данных.
data = cursor.fetchone()
print ("Database version : %s " % data)
 # Закройте соединение с базой данных
db.close()
def factorial(n):
   if n < 2:
       return 1
   return n * factorial(n — 1)

if __name__ == "__main__":
   n = int(input())
   print(factorial(n))



