
import psycopg2
from config import user,password,host,port,database
from psycopg2 import Error
try:
    # Подключиться к существующей базе данных
    connection = psycopg2.connect(
        user=user,
        password=password,
        host=host,
        port=port,
        database=database)
    connection.autocommit = True
    # Создайте курсор для выполнения операций с базой данных
    # cursor = connection.cursor() ЛИБО ЭТА СТРОКА ИЛИ WITH для работы с запросом 
    
    create_table_query = '''
;
    '''
    # Выполнение команды: это создает новую таблицу
    with connection.cursor() as cursor:
        cursor.execute(create_table_query)
    
    
    
    # cursor.execute(create_table_query)
    # connection.commit() # установли авто сохранение

except (Exception, Error) as error:
    print("Error when working with PostgreSQL", error)
finally:
    if connection:
        # cursor.close() # либо with 
        connection.close()
        print("Connection to PostgreSQL is closed")