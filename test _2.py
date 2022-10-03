import os
from datetime import datetime
from time import sleep
from mysql.connector import connect, Error

while True:
       'time out'
       sleep(30)
       'Get a files in directory'
       a = os.listdir('./log')
       'Print in shell names of files'
       print(a)
       'In a cicle from the files we get the values and after that we delete the files'
       for i in range(0, len(a)):
              file = open('./log/' + a[i], 'r', encoding='utf-8')
              l = file.readlines()
              v_0 = l[0][14:25]
              c_0 = l[1][13:25]
              r_0 = l[2][18:25]
              print(c_0)
              print(r_0)
              try:
                  with connect(
                          host="localhost",
                          user='root',
                          password='пщпщ123!',
                          database="values",
                  ) as connection:
                      print(connection)
                      insert_ratings_query = """
                      INSERT INTO system_indications
                      (Time, Name, Value)
                      VALUES ( %s, "%s", %s)
                      """
                      ratings_records = [
                          (str(datetime.now()), 'Voltage', v_0)
                      ]

                      with connection.cursor() as cursor:
                          cursor.executemany(insert_ratings_query, ratings_records)
                          connection.commit()
              except Error as e:
                  print(e)

              sleep(0.5)

              try:
                  with connect(
                          host="localhost",
                          user='root',
                          password='пщпщ123!',
                          database="values",
                  ) as connection:
                      print(connection)
                      insert_ratings_query = """
                      INSERT INTO current
                      (Time, Value)
                      VALUES ( %s, %s)
                      """
                      ratings_records = [
                          (str(datetime.now()), c_0)
                      ]

                      with connection.cursor() as cursor:
                          cursor.executemany(insert_ratings_query, ratings_records)
                          connection.commit()
              except Error as e:
                  print(e)

              sleep(0.5)

              try:
                  with connect(
                          host="localhost",
                          user='root',
                          password='пщпщ123!',
                          database="values",
                  ) as connection:
                      print(connection)
                      insert_ratings_query = """
                      INSERT INTO resistence
                      (Time, Value)
                      VALUES ( %s, %s)
                      """
                      ratings_records = [
                          (str(datetime.now()), r_0)
                      ]

                      with connection.cursor() as cursor:
                          cursor.executemany(insert_ratings_query, ratings_records)
                          connection.commit()
              except Error as e:
                  print(e)
              file.close()
              os.remove('./log/' + a[i])




