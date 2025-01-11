import psycopg2
connection = psycopg2.connect(database = "chinook")


cursor = connection.cursor() 
# cursor.execute('select * from "Artist"')
# cursor.execute('SELECT "Name" * FROM "Album"')
#cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ['Queen'])
 
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])
results = cursor.fetchall()
# results = cursor.fetchone()
connection.close()
print(results)
for result in results:
    print(result)