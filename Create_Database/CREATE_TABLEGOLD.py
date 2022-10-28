import psycopg2
from psycopg2 import Error 

try:
    connection = psycopg2.connect(user='webadmin',
                                    password='ZSAxvp50885',
                                    host='node38438-project.proen.app.ruk-com.cloud',
                                    port='11260',
                                    database='postgres')


    cursor = connection.cursor()

    create_table_guery = '''CREATE TABLE GoldAPI
        (D_M_Y VARCHAR(50) ,
        low_price     VARCHAR(50) ,
        high_price     VARCHAR(50) ,
        price_USD      VARCHAR(50)); '''

    cursor.execute(create_table_guery)
    connection.commit()
    print("Table created successfully in PostgreSOL ")

except (Exception, psycopg2.DatabaseError) as error: 
    print("Error while creating PostgreSQL table", error) 
finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSOL connection is closed")