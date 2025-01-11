import psycopg2
connection = psycopg2.connect(database = "chinook")


cursor = connection.cursor() 
cursor.execute('select * from "Artist"')
results = cursor.fetchall()
connection.close()
print(results)
for result in results:
    print(result)