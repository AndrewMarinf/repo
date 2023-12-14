
def create_database():
    # СОЗДАНИЕ БД 
    import psycopg2
    from psycopg2 import Error
    from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT 
    try:
        # Подключение к существующей базе данных
        connection = psycopg2.connect(user="postgres",
                                    # пароль, который указали при установке PostgreSQL
                                    password="9945",
                                    host="127.0.0.1",
                                    port="5432")
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        # Курсор для выполнения операций с базой данных
        cursor = connection.cursor()
        sql_create_database = 'create database sql_test'
        cursor.execute(sql_create_database)      
    except (Exception, Error) as error:
        print("Error when working with PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Connection to PostgreSQL is closed")
create_database()            