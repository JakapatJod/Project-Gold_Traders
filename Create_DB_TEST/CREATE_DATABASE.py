import psycopg2
try:
    connection = psycopg2.connect(user='webadmin',
                                    password='DMSgax19890',
                                    host='node38438-project.proen.app.ruk-com.cloud',
                                    port='11260',
                                    database='postgres')

    connection.autocommit = True

    #Creating a cursor object using the cursor() method
    cursor = connection.cursor()

    # Preparing query to create a database
    sql = '''CREATE database login'''

    #Creating  a database
    cursor.execute(sql)
    print('Database created sucessfully.........')

except (Exception,psycopg2.Error) as error:
    print('Error while connecting to PostgreSQL',error)
finally:
    # closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print('PostgreSQL connection is closed')