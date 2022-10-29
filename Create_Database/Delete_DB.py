import psycopg2
from psycopg2 import Error
try:
    connection = psycopg2.connect(user='webadmin',
                                    password='ZSAxvp50885',
                                    host='node38438-project.proen.app.ruk-com.cloud',
                                    port='11260',
                                    database='postgres')

    #Creating a cursor object using the cursor() method
    cursor = connection.cursor()

    deletes = '''DROP DATABASE login; '''

    cursor.execute(deletes)
    connection.commit()
    print('Delete database sucessfully in PostgreSQL ')
   

except (Exception,psycopg2.Error) as error:
    print('Error while connecting to PostgreSQL',error)
finally:
    # closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print('PostgreSQL connection is closed')